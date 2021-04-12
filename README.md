# lambda-calculus-translation-teamracket
lambda-calculus-translation-teamracket created by GitHub Classroom

Write a compiler that accepts terms in the lambda calculus and outputs either JavaScript or Python or (massively harder) C.

Here’s the grammar of the input language:
    LC	 	=	 	num 
    
 	 	|	 	id
 	 	|	 	(/ id => LC) 
 	 	|	 	(LC LC)     
            |	 	(+ LC LC)
 	 	|	 	(* LC LC) 
 	 	|	 	(ifleq0 LC LC LC)     (if then else)
 	 	|	 	(println LC) 
    
 ...where num is a number, and id is an identifier. 

The compiler created is in python and converts the lambda calc input to python. The resulting python code can be run to preform the actions that was desired from the lambda calculus that was input. There are test cases in the form of print statements in the original code with the compilers use also show by example in the main method. This can easily be extended to convert documents and other input sources due to the method call of the code and redirects available in python or linux.
