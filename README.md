# Shape Inference and Grammar Induction (SIGI) from Three-Dimensional Buildings
Implementation, examples and results for paper: Shape Inference and Grammar Induction for Example-based Procedural Generation

<p align="center"> 
    <img src="https://github.com/gillishermans/SIGI/blob/master/examples/example1.png" alt="">
 </p>

## Examples and Results
Examples used for testing and experiments are present in the folder /examples/.
We generated 10 new buildings for each example with and without enclosure for 20,50 and 100 production steps in the folder /results/.
These results were not cherry-picked and serve as a qualitative evaluation of the generative capabilities of the shape grammar.

<p align="center"> 
    <img src="https://github.com/gillishermans/SIGI/blob/master/results/Example1_50steps_enclosed/2021-03-20_23.44.37.png" alt="">
 </p>

Notes:
 - Some enclosed buildings contain buildings seperate from each other. These were connected by one or multiple uncenclosed shapes that were removed during enclosure.

## Implementation
### MCEdit
MCEdit can be deployed by following the instructions at https://github.com/Podshot/MCEdit-Unified.

### Filters
For the use of these filters they must be placed in the stock-filters folder within the root directory of the MCEdit repository. The filters can be applied by following these steps:
- start the MCEdit application as described at https://github.com/Podshot/MCEdit-Unified
- open a minecraft map (CTRL+O), such as the *example_world* map provided in the filter repository, by selecting the *level.dat* file in the map folder
- select the entire example structure or structures to be examined with the select tool
- apply the **infer_and_generate** filter with the filter tool to infer a set of shapes and a grammar and to immediately generate a new structure

### Filter Parameters
The **infer_and_generate** filter has a number of parameters:
- the hill climbing operation: 0 (only merge), 1 (only split), 2 (both)
- the shape specification: 0 (rectangular), 1 (planar), 2 (three-dimensional)
- the cost function: 0 (basic), 1 (multiple types cost increase), 2 (matching shapes discount)
- the α parameter: a value ∈ R
- is overlap of blocks in multiple shapes allowed: true or false
- is the post processing split operation allowed: true or false
- the amount of rule derivations allowed during automatic generation: 0 (no generation), any other positive value ∈ Z
- is the enclosure constraint enforced: true or false
- experimental split grammar option: true or false (no results guaranteed)
- visualization of overlapping generated shapes
