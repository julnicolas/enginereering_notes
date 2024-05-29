# CSS Selectors Cheat Sheet

By B Lingafelter     Apr 21, 2013      CSS, cheatsheets

Most web developers learn CSS by first writing style rules that target the HTML elements on the page because. the **element selector** is easy to understand and the results are immediate and obvious. With a little CSS practice, **grouped selectors** become essential to reducing redundancy because they allow us to apply the same style properties to multiple elements separated with commas in a single style rule.

The disadvantage of using element and grouped selectors of course, is that they are universally applied. And it doesn't take long before the need to format one particular element arises. The simplest solution for most developers is to use **class selectors** and **ID selectors** to target specific elements. But unfortunately, the tendency is to overuse them and end up with pages that suffer from class-itis.

Instead of mucking around with the markup by adding classes and id's to elements simply for styling purposes, consider using advanced CSS selectors to apply formatting to target elements. The many advanced selectors are generally categorized into **contextual selectors**, **attribute selectors**, **pseudo-element selectors**, and **pseudo-class selectors**.

## Element selectors

Element selectors apply properties globally to all specified elements on the page, and are the most common selectors used.

### Element

**h2**

selects all h2 elements on the page  
The rule **h2 {text-align: center;}** would center all text marked up with **<h2>** elements

### Grouped

**h1, h2, h3**

selects all h1, h2, and h3 elements on the page  
The rule **h1, h2, h3 {margin-bottom: .5em;}** would set the bottom margin for all text marked up with **<h1>**, **<h2>**, and **<h3>** elements

## Class and ID selectors

Class and ID selectors make it easy to target and apply properties to one or several particular elements without affecting all the others. Classes allow you to classify elements into conceptual groups. Two or more elements can belong to the same class on a page. IDs assign a unique identifier to an element, and _each id value must be used only once on a page_.

### Class

**.warning  
p.warning**

selects all elements belonging to the **warning** class  
selects only paragraph elements belonging to the **warning** class  
Note: **<p class="warning">** classifies the **<p>** into a conceptual group

### ID

**#links**

selects the element with the **links** id value  
Note: **<ul id="links">** assigns the links unique identifier to the element

## Contextual selectors

Contextual selectors (combinators) target elements based on their relationships to other elements in the document's tree hierarchy, and use the same _parent_, _child_, _sibling_, and _descendant_ terminology.

### Descendant

**#main li**

selects elements only when they are descendants of a higher-level element  
Note: target element does not have to be a direct child; descendant can be further down in hierarchy

### Adjacent sibling

**h2+p**

selects sibling element that is adjacent to (next to) another element  
(if there are several **<p>** elements following the **<h2>** element, only the first **<p>** is the adjacent sibling)

### Child

**blockquote>p**

selects elements only when they are child elements of the parent element

### General sibling

**h2~p**

selects any elements that are siblings to another element  
(if there are several **<p>** elements following the **<h2>** element, all are siblings)

### Related Links:

*   [The 30 CSS Selectors you Must Memorize](http://net.tutsplus.com/tutorials/html-css-techniques/the-30-css-selectors-you-must-memorize/)
*   [Taming Advanced CSS Selectors](http://coding.smashingmagazine.com/2009/08/17/taming-advanced-css-selectors/)

## Pseudo-class selectors

Pseudo-class selectors are used to apply styles to elements based on their browser state or position in document hierarchy. Browsers keep track of many things behind the scenes, like whether a link has been visited, when an element is selected, and whether an element is the first or last of its type, or even the first or last child of its parent element.

All elements in a certain state are treated as though they belong to the same class, even though the class name is not actually in the markup. Pseudo-class selectors are indicated by a colon (:), and are typically placed immediately after the element name.

### Pseudo-class selectors for link and user states

When styling all link states, the order of the rules in the style sheet is important for proper functionality. Required order is **:link**, **:visited**, **:focus**, **:hover**, **:active**.

#### Unvisited link

**:link**

applies to link elements that have not been visited (**a:link**)

#### Visited link

**:visited**

applies to link elements that have been visited (**a:visited**)

#### Focus state

**:focus**

applies to selected element that is ready for input  
(**a:focus** or **input:focus**)  
Note: focus state most often applies to users who use a keyboard to tab through links and form controls, but some elements can also be given focus with markup and scripts.

#### Hover state

**:hover**

applies when mouse pointer is over the element (**a:hover**)

#### Active state

**:active**

applies when element is in process of being clicked (**a:active**)

### Pseudo-class selectors that apply to siblings

The following six sibling pseudo-class selectors apply to elements that have the same parent, and are at the same level of the document hierarchy.

**:first-child**

selects the specified element when it is the first child of its parent  
(**h2:first-child** selects a **<h2>** element only when it's the first element within its parent)

**:last-child**

selects the specified element when it is the last child of its parent  
(**h2:last-child** selects a **<h2>** element only when it's the last element within its parent)

**:only-child**

selects the specified element when it is the only child of its parent  
(**h2:only-child** selects a **<h2>** element only when it's the only element within its parent)

**:first-of-type**

selects the first element of the specified type within its parent element  
(**li:first-of-type** selects the first **<li>** element)

**:last-of-type**

selects the last element of the specified type within its parent element  
(**li:last-of-type** selects the last **<li>** element)

**:only-of-type**

selects the only element of the specified type within its parent element  
(**blockquote p:only-of-type** selects the only **<p>** inside a **<blockquote>** element)

The **:first-child**, **:last-child**, and **:only-child** pseudo-classes are very specific. When a targeted element is no longer the first, last, or only child of its parent, the style rule no longer applies.

The other pseudo-classes are far more flexible. When you add or remove a targeted element, the browser will still automatically apply the style to the first and last element, or to the element that has no siblings of the same type.

#### Related Links:

*   [Meet the Pseudo Class Selectors](http://css-tricks.com/pseudo-class-selectors/)
*   [Getting to Know CSS3 Selectors: Structural Pseudo-Classes](http://www.sitepoint.com/getting-to-know-css3-selectors-structural-pseudo-classes/)
*   [Getting to know your CSS selectors Part 2: CSS3 pseudo-classes and pseudo-elements](http://www.adobe.com/devnet/dreamweaver/articles/css-selectors-pt2.html)

## CSS3 structural Pseudo-class selectors

The new CSS3 pseudo-class selectors can style elements based on their position within a series in the document hierarchy.

**:nth-child(n)**

nth child of parent

**:nth-last-child(n)**

nth child of parent counting backwards

**:nth-of-type(n)**

nth element of its type within parent

**:nth-last-of-type(n)**

nth element of its type counting backwards

Use the following typical n values to target elements.

Typical n values for CSS3 Structural Pseudo-class Selectors:

every odd child or element
---
2n+1

every even child or element
---
2n

every nth child or element
--
n

every third child or element (3, 6, 9, …)
--
3n

every third child or element starting with 1 (1, 4, 7, …)
--
3n+1

### Related Links:

*   [Useful :nth-child Recipes](http://css-tricks.com/useful-nth-child-recipies/)
*   [How To Use CSS3 Pseudo-Classes](http://coding.smashingmagazine.com/2011/03/30/how-to-use-css3-pseudo-classes/)
*   [Quick Tip: Work Backward to Understand Structural Pseudo Classes](http://net.tutsplus.com/tutorials/html-css-techniques/quick-tip-work-backward-to-understand-css-structural-pseudo-classes/)
*   [CSS3 Structural Pseudo-class Expressions Explained](http://www.impressivewebs.com/css3-pseudo-class-expressions/)
*   [How To Use Structural Pseudo Classes and Pseudo Element Selectors](http://www.vanseodesign.com/css/pseudo-elements-classes/)

## Pseudo-element selectors

Pseudo-element selectors allow you to style fictional elements that are not actually in the markup. The **::first-letter** and **::first-line** selectors target a portion of an element to avoid use of inline <span> element. The **::before** and **::after** selectors are used to insert content dynamically that doesn't exist in the markup.

CSS3 uses a double colon for pseudo-elements. To provide backward compatibility for older browsers, omit one of the colons that precede the pseudo-elements (ie **:first-letter**)

**::first-letter**

selects the first letter of the specified element  
(**p::first-letter** selects only the first letter of the **<p>** element)  
commonly used with **::first-child** to create a drop cap in first paragraph

**::first-line**

selects the first line of the specified element  
(**p::first-line** selects only the first line of the **<p>** element)  
commonly used with **::first-child** to add visual impact to the first line of the first paragraph

**::before**

adds generated content before the specified element when used with **content** property  
(**q::before {content: "\\201c";}** generates a left double quote before the <q> element)

**::after**

adds generated content after the specified element when used with **content** property  
(**q::after {content: "\\201d";}** generates a right double quote after the <q> element)

### Common uses of generated content:

``` css
    blockquote>p::before {
      content: "\201c"; /* left double quotation character */
      display: inline;
    }
    blockquote>p::after {
      content: "\201d"; /* right double quotation character */
      display: inline;
    }
```

Rules to style <blockquote> elements
``` css
    /*  apply class to  parent element to self-clear its floated children */
    .group:after {
      content: ""; 
      display: table; 
      clear: both; 
    }
```

Rule to force parent element to self-clear its floated children

### Related Links:

*   [Learning To Use The :before And :after Pseudo-Elements In CSS](http://coding.smashingmagazine.com/2011/07/13/learning-to-use-the-before-and-after-pseudo-elements-in-css/)
*   To find Unicode Characters:
    *   [Unicode Character Table](http://unicode-table.com/en/)
    *   [XHTML Character Entity Reference](http://www.digitalmediaminute.com/reference/entity/) - Hover over a character box to display the characters numerical code (&#8220;) and its Unicode code (u201c).  
        **NOTE:** For generated content with ::before and/or ::after pseudo-elements, use only the hexadecimal part--the part after the "u"--and be sure to escape the code by preceding with a backslash "\\" character.
*   [How To Benefit From CSS Generated Content And Counters](http://coding.smashingmagazine.com/2013/04/12/css-generated-content-counters/)
*   [How To Create a Stylish Drop Cap Effect with CSS3](http://line25.com/tutorials/how-to-create-a-stylish-drop-cap-effect-with-css3)
*   [CSS Fundamentals: Containing Children](http://net.tutsplus.com/tutorials/html-css-techniques/css-fudamentals-containing-children/)

## Attribute selectors

Attribute selectors target elements based on the presence or value of a specific attribute. Of the seven attribute selectors in the table below, the last three are new in CSS3, and are not yet fully supported by all browsers.

**E\[attr\]**

selects elements with specified attribute present, regardless of its value  
(**img\[alt\]** selects all **<img>** elements that have an **alt** attribute present)

**E\[attr="val"\]**

selects elements where the specified attribute has the exact value of **val**  
(**input\[type="text"\]** selects all **<input>** elements with **type** attributes that have a value of "text")

**E\[attr~="val"\]**

selects elements with attribute values that contain specified partial value of **val  
**(**img\[alt~="2014"\]** selects all **<img>** elements with **alt** attributes that contain "2014" in the whitespace seaparated value)

**E\[attr|="val"\]**

selects elements with attribute values that contain hyphenated value that starts with **val** and is immediately followed by "**\-**"  
(**img\[src|="thumb"\]** selects all **<img>** elements where the **src** attribute value contains "thumb-")

**E\[attr^="val"\]**

selects elements where the value of the specified attribute begins with **val**  
(**a\[href^="http"\]** selects all **<a>** elements where the **href** attribute value begins with "http" —identifies external links)

**E\[attr$="val"\]**

selects elements where the value of the specified attribute ends with **val**  
(**a\[href$=".pdf"\]** selects all **<a>** elements where the **href** attribute value ends with ".pdf" —identifies links to PDF files)

**E\[attr\*="val"\]**

selects elements where the value of the specified attribute contains **val**  
(**img\[src\*="thumb"\]** selects all **<img>** elements where the **src** attribute value contains "thumb" —identifies images with thumb in filename as well as images in thumbs folder)

### Related Links:

*   [Quick Tip: Make the Most of CSS Attribute Selectors](http://webdesign.tutsplus.com/tutorials/htmlcss-tutorials/quick-tip-make-the-most-of-css-attribute-selectors/)
*   [Getting to know your CSS selectors Part 1: CSS2.1 and attribute selectors](http://www.adobe.com/devnet/dreamweaver/articles/css-selectors-pt1.html)
*   [The Skinny on CSS Attribute Selectors](http://css-tricks.com/attribute-selectors/)

**Disclaimers:** [Butler Community College](https://www.butlercc.edu/) is an “Equal Opportunity Employer/Program” and “Auxiliary Aids and Services are available upon request.”

[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/) This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

Generously Provided by  
[![Butler Community College](/images/Butler_Horiz_206a.png)](https://www.butlercc.edu/)
