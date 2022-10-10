# How to Create requirements.txt file in Python

In this tutorial I go over:
- What is the requirements.txt file? 
- How is it made?
- How to use it? 
- And, why is it necessary?


[![Video Thumbnail](Thumbnail.png)](https://www.youtube.com/watch?v=kGWsVwZr0ek)


## What is requirements.txt?

'requirements.txt' is a text file containing the list of external python libraries along with their versions, needed in order to run the python files in a specific directory.

## How is it made?

To create a requirements.txt file we require another external python library - pipreqs

Type in terminal
```terminal
pip install pipreqs
```

Once you've successfully installed pipreqs, navigate to the directory containing your file.

Type in terminal
```terminal
cd "path to directory"
```

After navigating your terminal to the correct directory run pipreqs.

Type in terminal
```terminal
pipreqs
```

Alternatively, after installing pipreqs, you can run the command

Type in terminal
```terminal
pipreqs "path to directory"
```

## How to use it?

Now that you have successfully made a requirements.txt file, let us understand how you can use it.

Type in terminal
```terminal
pip install -r requirements.txt
```

The above command parses through the requirements.txt file and installs each external library's specified version.

## Why is it neccesary?

Imagine a scenario, where you are working on a programming project with friends, or on an open source project with strangers online.

When you create a big/complex program it is highly likely that you use an external library.

Many times the library you use maybe a common one and everyone using your code would have it installed, but there is a possibility of having different versions of the same library, which might cause the code to work differently on different machines.

Or in an event where the libraries you use are not common and may not be installed on the machines of those that try and run your code.

To ease this proccess of manually installing each library which is used in the code, we use requirements.txt, so that all the libraries being used could be installed at once.

In another scenario where you are not sharing your code with other people but using it on different machines, it eases the proccess of installing the required libraries, to ensure smooth execution of your code!