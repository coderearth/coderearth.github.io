Title: "A Polyglot's Guide To Elegant Fibonacci"
Date: 2014-11-19 12:21
Category: Blog


The Fibonacci numbers originally seen in [Indian Mathematics](http://en.wikipedia.org/wiki/Fibonacci_number#Origins), appeared in the West in the form of Liber Abaci by Leonardo of Pisa, known as Fibonacci. The series is known to manifest itself in nature in [various ways](http://en.wikipedia.org/wiki/Fibonacci_number#In_nature).

The idea of this blog post is to find out the N<sup>th</sup> fibonacci number programmatically in many of today's modern programming languages, <i>as elegantly  as possible</i>, while closely resembling the above mathematical relation.

The  series is defined by the following recurrence relation,

$$F_n = F_{n-1} + F_{n-2}$$ 

with seed values - $F_1 = 1,\ F_2 = 2$ or $F_0 = 0,\ F_1 = 1$.

### Haskell


~~~ Haskell
fib n = if n < 2 then n else fib(n-1) + fib(n-2)
~~~


or alternatively,

~~~ Haskell
fib 0 = 0
fib 1 = 1
fib n = fib(n-1) + fib(n-2)
~~~ 

Here's a copy paste from my `ghci` shell,

~~~ haskell
Prelude> let fib n = if n < 2 then n else fib(n-1) + fib(n-2)
Prelude> fib 10
55
Prelude> fib 11
89
Prelude> fib 12
144
~~~


The above piece of code will just give us the N<sup>th</sup> fibonacci. If however we want to get fibonacci numbers up until an N, then we can do something like this,

~~~ haskell
Prelude> map fib [1..10]
[1,1,2,3,5,8,13,21,34,55]
~~~

### Python

~~~ python
In [1]: fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)

In [2]: fib(10)
Out[2]: 55

In [3]: fib(11)
Out[3]: 89

In [4]: fib(12)
Out[4]: 144

In [5]: map(fib, range(10))
Out[5]: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
~~~


Alternatively,

~~~ python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
~~~

### C++

~~~ cpp
#include <iostream>
int fib(int n) {
    if (n == 0) return 0;
    else if (n == 1) return 1;
    else return fib(n-1) + fib(n-2);
}

int main() {
    for (int i=0; i<10; ++i) 
        std::cout<<fib(i)<<"\n";
    return 0;
}
~~~

### Ruby

~~~ ruby
def fib(n)
  n < 2 ? n : fib(n-1) + fib(n-2)
end

1.upto(10) { |i| puts fib(i) }
~~~

Alternatively, a beginner's version would look like this,

~~~ ruby
def fib(n)
  case
  when n < 2
    n
  else
    fib(n-1) + fib(n-2)
  end
end

for i in 1..10 do
  puts fib(i)
end
~~~

More languages to follow soon.

The <i>elegance</i> here is a small compromise as far as performance is concerned, there are ways to increase computation speed which will be discussed in an upcoming post titled <i> A Polyglot's Guide to Fast Fibonacci </i>.