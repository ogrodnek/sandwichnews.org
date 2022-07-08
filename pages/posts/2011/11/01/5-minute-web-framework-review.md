title: 5 minute web framework review - reading params
date: 2011-11-01T10:00:00
tags: [technology, web]

Through various experiments, hackdays, conversations with other developers, etc. I've found myself experimenting with a few different web frameworks. The focus has been mostly simple webapps / simple REST services written in scala that return html or json. I thought it might be interesting to dive into some focused comparisons in a series of posts.

This is not an exhaustive comparison. I'm going to be focusing on the frameworks I've found the most interesting for my use cases lately, namely [scalatra](https://scalatra.org/), [play](https://www.playframework.com/), and [jersey](https://eclipse-ee4j.github.io/jersey/).

For the first comparison, I want to focusing on reading query and path parameters. Parameter de-serialization has always been a pain. The web uses strings, and strings are messy. Are my required params specified? Are they the right types? Can I easily convert to the types my program expects? Do they pass my validation? etc.

Let's look at how each framework helps us deal with these common concerns.

# jersey

I like jersey. It's a reference implementation of JSR-311: Java API for RESTful Web Services. It's also quite nice to work with in scala.

## query parameters

With jersey, query parameters are simply specified as method parameters. Simple types are automatically converted, and it's easy to specify defaults. It will also automatically call converters for use with your own complex types. Unfortunately, you must use annotations to map query param names to method params.

```scala
def doGet(@QueryParam("name") name: String,
@QueryParam("count") @DefaultValue("2") count: Int): String = {
  "name: %s, count: %d\n".format(name, count)
}
```

It works pretty much as you'd expect:

```
$ curl "http://localhost:8080/hello?name=larry&count=5"
name: larry, count: 5
```

If the types aren't correct, you'll get a 404:

```
curl "http://localhost:8080/hello?name=larry&count=a" -D -
HTTP/1.1 404 Not Found
```

## path parameters

Path parameters in jersey work pretty much the same way as query params, i.e. typed, with default values and appearing as method arguments. Additionally you can do some simple validation using regular expressions. Their names and path location are specified when defining the route.

```scala
@Path("/hello/{userid}")
class Hello {
  def doGet(@PathParam("userid") id: Int)
}
```

Here's a different example showing some simple regex validation support:

```scala
@Path("/hello/{username: [a-zA-Z][a-za-z_0-9] }")
```

And, again, if the path doesn't match your regex, or type, you will get a 404.

## other params

There are also `@CookieParam`, `@HeaderParam` annotations for reading cookie and header values, as well as support for pulling in session or request variables using @Context or custom annotations (e.g. I've created `@IpAddress` for pulling in the ip).

## overall thoughts

I really like the automatic de-serialization and type conversion, and having the framework handle errors for incompatible parameters automatically.

I also like the POJO mindset. It's just a function with arguments like any other. All else being equal, this makes testing in any framework super easy.

The annotations do seem a little noisy, especially having to specify the parameter name. I think we can do better.

# scalatra

scalatra is also very nice for simple apps, and I've quickly become a fan of scalate which it uses for templating.

When it comes to dealing with parameters though, it feels like a step back. Everything is strings. The fact that it's scala makes it easier to deal with, but it does feel like the framework could go a little further to help you out.

## query parameters

To read query parameters, you use the params method from ScalatraServlet. Params is a `MultiMapHeadView[String, String]`. So yes, you are back to dealing with Strings (or a `Seq[String]` if using multiParams).

```scala
get("/hello") {
  val name:String = params.getOrElse("name", halt(400))
  val count:Int = params.getOrElse("count", "2").toInt

  "name: %s, count: %d\n".format(name, count)
}
```

Calling this path without a name will generate a 400, as expected:

```
$ curl "http://localhost:8080/hello" -D -
HTTP/1.1 400 Bad Request
```

If you don't specify count, you will get the default of 2. However, if you specify a non-int, you'll get a 200 where the contents are the stack trace for the toInt call. Again, your validation is all manual -- if you want better type validation, it's up to you.

```
$ curl "http://localhost:8080/hello?name=larry&count=a" -D -
HTTP/1.1 200 OK
…


java.lang.NumberFormatException: For input string: "a"
```

## path parameters

Path params work exactly the same way (including being accessed in params), and are named as part of your route

```scala
get("/hello/:name/:count") {
  val name:String = params.getOrElse("name", halt(400))
  val count:Int = params.getOrElse("count", "2").toInt

  "name: %s, count: %d\n".format(name, count)
}
```

```
$ curl "http://localhost:8080/hello/larry/5"
name: larry, count: 5
```

## overall thoughts

The manual de-serialization seems a little dated, and gets old quick. Scala does make it nicer than it would be in java, since you can do things like params.`getOrElse("name", halt(400)`), but I would like to see more.

I also miss the POJO mindset… when testing you need to do whatever additional setup is necessary to serialize your params as strings and stick them in a map.

I guess I also don't like that barring convention, there's no formal definition of what parameters you are expecting and what their types are - maybe you are calling params.get somewhere in the middle of your method..

# play

play the framework feels a little heavy compared to jersey and scalatra, but if definitely shines when it comes to dealing with parameters.

## query parameters

Query parameters in play are done really well. It's almost perfect.

```scala
def hello(name: String, count: Int = 2) = {
  "name: %s, count: %d\n".format(name, count)
}
```

```
$ curl "http://localhost:9000/hello?name=larry"
name: larry, count: 2
```

You can even use Option for parameters that may be available:

```scala
def hello(name: Option[String], count: Int = 2) = {
  "name: %s, count: %d\n".format(name.getOrElse("anon"), count)
}
```

One problem is that type conversion errors are silently ignored, and defaults will be used:

```
$ curl "http://localhost:9000/hello?name=larry&count=a"
name: larry, count: 2
```

Okay, so they're not really ignored. If you call `Validation.hasErrors`, it will return true, and you can discover the error. This is the same mechanism you need to use to mark parameter as required:

```
def hello(name: String, count: Int = 2) = {
  Validation.required("name", name)
  if (Validation.hasErrors) {
  // handle error
  }
}
```

## path parameters

Path parameters work the same way. They're defined with placeholders in your route, and automatically passed in as the correct argument. In play, routes are defined external to your code, in a routes file. E.g.

```
GET /hello/{name} Application.hello
```

Our method looks the same as the first Query param example. Calling it looks like this:

```
$ curl "http://localhost:9000/hello/larry"
name: larry, count: 2
```

In the case of path parameters, we will get a 404 if missing the parameter (since it won't match our route).

```
$ curl "http://localhost:9000/hello/" -D -
HTTP/1.1 404 Not Found
```

## overall thoughts

Overall I think parameters in play are done really well.

Like jersey, I really appreciate the POJO approach. play does it even better by eliminating the extra annotations and leveraging scala's default argument support.

Validation does seem a little clunky, though. It seems like more could be done there.
