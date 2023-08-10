# Meaning of 'mixin'

A `mixin` can refer to two related things depending on what the writter means:
- either a `mixin` class which is a feature oriented class, designed to be inherited
from to provide an extra set of features to the child class through `multiple inheritance`.
It can be thought of as a `component class`. An example would be to provide `oauth` capabilities
to a Request class for instance.
- or it can be the `mixin relationship` which is a `(multiple) inheritance` relationship. Mixin
base classed are inherited. If several mixins are enabled then multiple inheritance happens.


## Conclusion
This pattern provides the exact same functionnalites than composition (whether dependency injection
is used or not) but it introduces the following problems:
- risk of having a `diamond inheritance problem`
- change of object behaviour implies modifying a class (not `SOLID`), edit in the class definition
as inherited classes must be changed (not `SOLID` either)
- it is harder to test as "mixined" components are part of the base class rather than injected.

However, it can be useful to provide an extra set of core behaviours and interfaces as part of a child
class without introducing the creation of new objects at run time (and the extra memory consumption that
it may entail). However, `diamond inheritance` is still a danger so base-classes' inheritance chains must
be as shallow as possible to mitigate this risk (that would ease control by humans or tools).

Finally, dependency injection and composition is generally the simplest, most reliable  and most robust 
pattern to use. However, Mixin can be great for an object to inherit base interfaces and leverage polymorphism.
Though, `diamond inheritance patterns` must be checked after really carefully.
