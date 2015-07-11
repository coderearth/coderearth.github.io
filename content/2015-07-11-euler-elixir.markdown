Title: Project Euler With Elixir Lang
Date: 2015-07-11 22:00
Category: Programming
Authors: Suhas
Tags: Elixir, Erlang, Functional Programming
Summary: Elixir is a dynamic, functional language designed for building scalable and maintainable applications. Project Euler is a series of challenging mathematical/computer programming problems that will require more than just mathematical insights to solve.

Elixir is a dynamic, functional language designed for building scalable and maintainable applications. Elixir is built on top of the Erlang VM, the same VM known for helping WhatsApp scale to the extent that it is today. Learning any language is simpler when one actually writes code in it, and read lots of well-written code. In that spirit, I've started solving [Project Euler](https://projecteuler.net/) with Elixir.

### [https://github.com/jargnar/euler-elixir](https://github.com/jargnar/euler-elixir)
---

Here's an excerpt:

~~~ elixir
# Find even fibonaccis less than 4000000

fibs = Stream.unfold({0, 1}, fn {a, b} -> {a, {b, a + b}} end)
fibs
  |> Stream.reject(fn(x) -> rem(x, 2) != 0 end)
  |> Enum.take_while(fn(x) -> x < 4000000 end)
  |> Enum.sum
~~~