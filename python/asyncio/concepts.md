# Concepts

Asyncio is a library which implements a task scheduler for python. It uses a 
`cooperative multitasking` model. This library enables multi tasking capabilites
for the python language.

As my current understanding is, tasks are executed in a single thread, unless
explicitely comunicated to asyncio with the function `asyncio.to_thread`.

Asyncio tasks are implemented using python `coroutines`.

A python coroutine is a function defined using the `async def` keywords.

## Definition of a cooperative multi tasking model

A cooperative multi tasking model is a task execution model where
tasks are able to interupt themselves explicetely, leaving time for  other tasks
to execute.

This model can be very suited for IO tasks which waiting time can be very long.

To my experience, this model is often implemented using coroutines.

Coroutines are routines able to interrupt explictely and resume execution from
interruption when called. They often use the `yield` keyword to do so. In python
however, this key word is reserved to implement generator objects. Interuption
for the python coroutine object is carried out using the `asyncio.sleep` function.

## Main asyncio components
- `Task`: a task is a user provided coroutine object whose execution is
    managed (ran then resumed if needed) by asyncio. Tasks are created with
    `asyncio.create_task`
- `TaskGroup`: a task group is an aggregate of tasks. They are used to batch
    await operations on the whole group
- `Future`: low level asyncio object. One of the building blocks of the Task
    class. For most usage tasks are the way to go.
- `loop`: loops correspond to a thread executing tasks. Triggering loops
    execution is done using `asyncio.run`.

## Comparison between python generator and coroutine objects
One way to define a generator object is as follows:

``` python
def f():
    for i in range(0, 4):
        yield i

# Instantiate a generator object
g = f()
for i in g:
    print(i) # prints 0, 1, ... 3
```

Then every call to f().__next__  will return i ( 0 <= i <= 3). Every call is interupted
at the `yield` statement. Then resumed from the statement following the last yield when
__next__ is being called again. Per the precedent section, these are the properties of 
a coroutine, therefore a generator is a coroutine.

However generator objects are of the `generator` type and not from the coroutine type.

The coroutine type implements the `__await__` method making it possible to use the
`await` key word.

They are defined and called as follows:
``` python
async def f():
    # do things

    # this is equivalent to a yield statement, it is actually implemented
    # using yield so that execution can be resumed after
    await asyncio.sleep(0)
    # do other things

async def main():
    t1 = asyncio.create_task(f())
    await t1

asyncio.run(main())
```

Asyncio expects coroutines of the python type `coroutine`. Passing a `generator` to
`create_task` raises a `RuntimeError("Task got bad yield")`. An interesting thing to
notice here is the 'bad yield' part... yes, `coroutine` objects are implemented using
the `yield` instruction as generator objects are! (which is totally logical because
this is how the concept of coroutine is implemented in python). Though, some meta-data
are changed to make these two objects archetypes different.
