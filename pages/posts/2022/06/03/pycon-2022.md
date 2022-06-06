title: PyCon 2022
date: 2022-06-03T18:00:00
tags: [technology]

[Videos from PyCon 2022](https://www.youtube.com/playlist?list=PL2Uw4_HvXqvYeXy8ab7iRHjA-9HiYhRQl) are online. I've only made it through a few so far, but they've been great. I thought I'd write up a quick summary and some thoughts on the sessions I've been able to catch.

## Brandt Bucher: A Perfect Match The history, design, implementation, and future of Python's structural pattern matching

[Talk Video](https://youtu.be/XpxTrDDcpPE)

Brandt is the author of the specification for adding Pattern Matching to Python (in 3.10). The original spec [PEP 622](https://peps.python.org/pep-0622/) was later replaced with a series of PEPs, one for the spec [PEP 634](https://peps.python.org/pep-0634/), one for the motivation and rationale [PEP 635](https://peps.python.org/pep-0635/), and an introductory tutorial on using pattern matching in python [PEP 636](https://peps.python.org/pep-0636/).

I'm a big fan of pattern matching from my scala days and I'm excited to see it land in python. The implementation was obviously inspired by other languages, but in a way that feels at home in python.

Pattern matching makes it really easy and clear to pull apart and match against data structures.

An example from the [tutorial](https://peps.python.org/pep-0636/):

```python

@dataclass
class Click:
    position: tuple
    button: Button

match event.get():
    case Click((x, y), button=Button.LEFT):  # This is a left click
        handle_click_at(x, y)
    case Click():
        pass  # ignore other clicks
```

You can see how easy it is to destructure the `Click` dataclass and use its attributes in our match.

I'm really excited this has landed in python and can't wait to start using it in my own code.

# Fred Phillips: Hooking into the import system

[Talk Video](https://youtu.be/ziC_DlabFto)

I've never really thought about it, but the import system in python is dynamic and you can provide your own import resolvers fairly easily. I guess it's somewhat similar to something like [Classloaders](https://www.baeldung.com/java-classloaders) in Java.

In this talk, Fred walks through simplified versions of real world import hooks he's written/used in production, including a "Blocklist" loader (raises errors if the import is included in a blocklist), and a DB Loader (loads python code from the DB on import), as well as a tracing loader that prints out imports as they are happening.

Looking into this more, I discovered [an example import finder implementation on Real Python](https://realpython.com/python-import/#example-automatically-install-from-pypi) that attempts to pip install modules as they are being imported.

While loading code from a DB kind of scares me, it was a really interesting talk and this is something I definitely want to play with more.

Related there's a draft PEP for making imports lazy [PEP 690](https://peps.python.org/pep-0690/).

## Jeremiah Paige: Intro to Introspection

[Talk Video](https://youtu.be/2XDT37Tbv9c)

Python has always been interesting to me w.r.t. how much information is available to inspect at runtime from your code.

For example, given a method with a docstring comment, like:

```
def my_method():
    """
    This method does something amazing!
    """
    pass
```

One can access the docstring with `my_method.__doc__` and see that comment. You can even access the source by using `inspect.getsource(my_method)`! This kind of stuff blows my mind coming from other languages. Obviously there's a lot more useful stuff you can get including typing information, call signatures, etc. In this talk, Jeremiah walks through the basics of introspection in python, with an eye towards demystifying how the python `help` command could be implemented. Definitely worth checking out!

## Anthony Shaw: Write faster Python! Common performance anti patterns

[Talk Video](https://www.youtube.com/watch?v=YY7yJHo0M5I&t=1615s)

Anthony also discusses [perflint](https://github.com/tonybaloney/perflint) a linter that he's written to check for some of these performance anti-patterns. As he's mentioned in the talk and the readme, it's currently pretty early and will raise false positives (can confirm), but it's a great idea and definitely worth checking out for any performance sensitive code.

## Bruce Eckel: Making Data Classes Work for You

[Talk Video](https://youtu.be/w77Kjs5dEko)

Bruce talks about encapsulating validation logic into your Data Classes using `__post_init__()` (and `frozen=True`).

As an example, he goes through using a `Stars` dataclass, that basically wraps an `int`, but restricts it to be in some range. Then any functions that take or return `Stars` are easy to reason about.

It seems like a good strategy for ensuring consistency and safety in your code.

Classes are not types, but it reminded me a bit about phantom types in Scala.
