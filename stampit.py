# This script is a command-line utility that takes an input file, a stamp file, and an output file as arguments.
# It puts stampfile on every page of the input file and saves the result to the output file.

import sys, getopt, pymupdf

def stampit(inputfile, stampfile, outputfile):
    # Open the input PDF file
    doc = pymupdf.open(inputfile)
    
    # Open the stamp PDF file
    stamp = open(stampfile,"rb").read()

    #Set the stamp position on the page
    rect = pymupdf.Rect(350, 700, 400, 750)
    img_xref = 0
    
    # Iterate through each page of the input PDF
    for page in doc:
        # Insert the stamp on the current page
        img_xref = page.insert_image(rect, stream=stamp, xref=img_xref)
    
    # Save the modified PDF to the output file
    doc.save(outputfile)
    
    # Close the documents
    doc.close()

def main(argv):
    argumentList = argv
    options = "hf:s:o:"
    long_options = ["help", "input", "stamp", "output="]

    try:
        arguments, values = getopt.getopt(argumentList, options, long_options)
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-h", "--help"):
                print("Usage: stampit.py -f <inputfile> -s <stampfile> -o <outputfile>")
                sys.exit()
            elif currentArgument in ("-f", "--input"):
                inputfile = currentValue
                print(f"Input file: {inputfile}")
            elif currentArgument in ("-s", "--stamp"):
                stampfile = currentValue
                print(f"Stamp file: {stampfile}")
            elif currentArgument in ("-o", "--output"):
                outputfile = currentValue
                print(f"Output file: {outputfile}")
    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))
        print("Usage: stampit.py -f <inputfile> -s <stampfile> -o <outputfile>")
        sys.exit(2)
    
    # Check if inputfile and outputfile are provided
    if 'inputfile' not in locals() or 'stampfile' not in locals() or 'outputfile' not in locals():
        print("Usage: stampit.py -f <inputfile> -s <stampfile> -o <outputfile>")
        sys.exit(2)
    
    # Check if inputfile exists
    try:
        with open(inputfile, 'r') as f:
            pass
    except FileNotFoundError:
        print(f"Error: The file {inputfile} does not exist.")
        print("Usage: stampit.py -f <inputfile> -s <stampfile> -o <outputfile>")
        sys.exit(2)
    
    # Check if stamp exists
    try:
        with open(stampfile, 'r') as f:
            pass
    except FileNotFoundError:
        print(f"Error: The file {stampfile} does not exist.")
        print("Usage: stampit.py -f <inputfile> -s <stampfile> -o <outputfile>")
        sys.exit(2)
    # Check if outputfile is writable
    try:
        with open(outputfile, 'w') as f:
            pass
    except IOError:
        print(f"Error: The file {outputfile} is not writable.")
        sys.exit(2)
    
    # Check if inputfile is a valid file
    try:
        with open(inputfile, 'r') as f:
            pass
    except IOError:
        print(f"Error: The file {inputfile} is not a valid file.")
        sys.exit(2)
    
    # Check if stampfile is a valid file
    try:
        with open(stampfile, 'r') as f:
            pass
    except IOError:
        print(f"Error: The file {stampfile} is not a valid file.")
        print("Usage: stampit.py -f <inputfile> -s <stampfile> -o <outputfile>")
        sys.exit(2)

    stampit(inputfile, stampfile, outputfile)
    print(f"Stamping {inputfile} with {stampfile} and saving to {outputfile}")
    
if __name__ == "__main__":
    main(sys.argv[1:])

