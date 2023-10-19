# Hello World in 64-bit Assembly

## Installing dependencies

```sh
sudo apt install binutils nasm
```

## Compiling and running

The `-f elf64` flag below tells the compiler that the source uses 64-bit instructions

In a terminal:

```sh
cd assembly-example
nasm -f elf64 hello.s  # Compile source to object file that contains machine code
                       # and usually also references to functions or variables found
                       # in other object files or libraries.
ld hello.o -o hello    # Link object file and create executable. Normally,
                       # the machine code of several object files are here combined into
                       # one executable, but references to dynamic libraries are kept.
./hello                # Run executable
```

## Verify standard error
To confirm that the output is directed to standard error and not standard output, you can redirect the standard error stream to a file named stderr.txt. After running the program, inspect stderr.txt to ensure it contains the expected messages.

```sh
./hello 2> stderr.txt
```

![Output](https://github.com/ecschoye/idatt2503/blob/main/exercises/04/01/output.png)

To check that the program returns the correct error code, use the echo $? command immediately after executing your program. This will display the return code of the last executed command.

```sh
echo $?
```

![Verify Standard Error](https://github.com/ecschoye/idatt2503/blob/main/exercises/04/01/verify_standard_error.png)


If it returns 1, this confirms that your program has successfully returned an error code of 1, indicating an error occurred as expected.

By following these steps, you can validate both the output stream and the returned error code of your assembly program.
