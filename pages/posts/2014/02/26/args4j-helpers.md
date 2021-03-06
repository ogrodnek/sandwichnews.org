author: larry ogrodnek
title: args4j-helpers
date: 2014-02-26T12:00:00
tags: [technology, code, scala]

I really like using [args4j](http://args4j.kohsuke.org/) for command-line parsing in both java, and scala, but I found myself writing the same boilerplately code to parse options, deal with help, deal with parsing issues, etc.  [args4j-helpers](https://github.com/ogrodnek/args4j-helpers) is a project that simplifies parsing with args4j.

It provides typical option parsing error handling:

* If help (provided via `OptionWithHelp` base trait bound to `--help` and `-h`) is requested, print usage information to stderr, exit with code `0`.
* If a required option is missing (`required=true`), print usage information to stderr, exit with code `1` (unless help was requested).


This typical parsing code:


    class Options {
      import org.kohsuke.args4j.Option
    
      @Option(name="--help", aliases=Array("-h"), usage="show this message")
      var help = false
  
      @Option(name="--blah", aliases=Array("-b"), usage="some val", metaVar="BLAH")
      var blah: Int = 0
    }
  
    def main(args: Array[String]) {
      val options = new Options
      val parser = new CmdLineParser(options)
    
      try {
        parser.parseArgument(args : _*)
      
        if (options.help) {
          parser.printUsage(System.err)
          sys.exit(0)
        }
      } catch {
        case e: CmdLineException => {
          System.err.println(e.getMessage)
          parser.printUsage(System.err)
          sys.exit(1)
        }
      }
    }


can be simplified as:

    class Options extends OptionsWithHelp {
      import org.kohsuke.args4j.Option
  
      @Option(name="--blah", aliases=Array("-b"), usage="some val", metaVar="BLAH")
      var blah: Int = 0
    }
  
    def main(args: Array[String]) {
      val options = optionsOrExit(args, new Options)
    }


Additionally, the helper class handles the case where help is requested and required arguments are missing (which is missing from the simplified boilerplate code).

The code is in scala, and [available on github](https://github.com/ogrodnek/args4j-helpers).

In the future, I'd like to extend it to add better support for more scala-ish types (`Option`, `Seq`, etc., which should be mostly possible by implementing additional args4j OptionHandlers).


