# Rust-Python interop

Simple example of interop between Rust on C ABI and Python `ctypes` built-in package.

Rust exported function is marked as no mangle (so that it is easily accessible when specified in
Python), as well as using the C calling convention (C ABI).

Python on the other hand specifies how it should be calling the function. In there the
implementations in pure Python and in Rust are compared using a simple timing test.

## Usage

- If you are on Windows x64 you can easily grab the DLL and Python script on the
  [Releases page](https://github.com/kirillsemyonkin/rust-python-interop/releases).

- To compile Rust code yourself, you can use [the usual rust tools](https://www.rust-lang.org/tools/install),
  like `cargo build --release`, followed by a copy of the resulting DLL/SO files from the
  `target/release` directory, substituting the actual filename in [the `.py` file](python.py) if
  necessary.
