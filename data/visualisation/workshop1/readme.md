# Lecture 1 - Data Visualisation

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Lecture 1 - Data Visualisation](#lecture-1---data-visualisation)
    - [Textbook](#textbook)
    - [What?](#what)
    - [Datatypes](#datatypes)
        - [How to visualise these datatypes?](#how-to-visualise-these-datatypes)
        - [Categorical](#categorical)
            - [Channels](#channels)
        - [Ordered](#ordered)
            - [Channels](#channels-1)
        - [Saturation vs Brightness vs Hue](#saturation-vs-brightness-vs-hue)
    - [Dataset Types](#dataset-types)
        - [Grid](#grid)
    - [Example Visualisation](#example-visualisation)
        - [B. Heap map of Australia showing travel time](#b-heap-map-of-australia-showing-travel-time)

<!-- markdown-toc end -->


## Textbook
* Visualisation Analysis and Design



```
What? ---------------------------------> How?
```

## What?

* Attribute types
	* Ordered
		* Ordinal
	* Quantitative

## Datatypes
* Item
* Table
* Attribute
  * Categorical/nominal
  * Ordered
    * Ordinal
    * Nominal
    * Quantitative
      * Time, temperature etc
* Link
* Position
* Grid

### How to visualise these datatypes?

### Categorical
####  Channels
* Hue
* Shape

### Ordered
* Marks
  * TODO
#### Channels
  * Position
  * Tilt/orientation/angle
  * Size: Length
  * Size: Area
  * Size: Volume 
    * Sphere
    * Cube
  * Value/brightness/luminance
  * Saturation
  * TODO


### Saturation vs Brightness vs Hue
| Saturation                               | Brightness                        | Hue |
|:----------------------------------------:|:---------------------------------:|:---:|
| Goes to gray on one end (more grayscale) | Goes from very white to very dark |     |
|                                          |                                   |     |


## Dataset Types
* Table
* Network
* Tree
* Field
* Geometry

### Grid

```
      position x = ...
y     / 
|    * . . . . . .
|    . . . . . . .
|    . . . . . . .
|    . . . . . . .
|    . . . . . . .
|    . . . . . . .
|    . . . . . . . |
|    . . . . . . . | 20m
_________________________> x
```


## Example Visualisation

| Type                  | A            | B                               | C             | D                            | E                               | F                                   | G         |
|-----------------------|:------------:|:-------------------------------:|:-------------:|:----------------------------:|:-------------------------------:|:-----------------------------------:|:---------:|
| DataType              | grid         | Map                             | Bar Chart     | Table                        | Map                             | Geometry                            | Bar Chart |
| Attributes            | Quantitative | Quantitative                    | Quantitative  | Quantitivate and Qualitative | Quantitive                      |                                     |           |
| Derived Dataset Types | Position     | Field (for storing travel time) | Position      | Position                     | Table contains position         | Field (elevation), network for flow | Position  |
| Categorical           | Position     | Position                        | Position      | Position                     | Hue (for either Macron and Pen) | Position                            | Position  |
| Ordered               | Size (area)  | Brightness+Hue                  | Size (length) |                              | Area                            |                                     |           |
| Marks                 |              |                                 |               |                              |                                 |                                     |           |


### B. Heap map of Australia showing travel time
A field with grids and travel time in each cell

* Sometimes combintation of Hue and brightness can be used to represent **quantitative channel**.

### C. Bar chart Lego's first half revenue each each with cool lego visuals
* Hue and brightness can be ornamental (for asthetics) meaning that it does not represent any channels.


### D. A Bar Chart With Volume Of Tweets For Twitter User Sentiment On Will Smith Before And After Slap


### E. Map of votes for Macron and Le Pen in France

### D. Map Of The Whole World From National Geographics
