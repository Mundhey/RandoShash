
# RandoShash

Solving ASIC Resistance Problem in Cryptocurrency Mining


## RandoShash Overview
Approach is to use a Random sequence of hashing algorithms based on hash of previous block, where the output of one becomes the input to the next

[Project Website](https://mundhey.github.io/RandoShash/)

<!---
## Review of Existing PoW Algorithm

### SHA256 [Project](https://github.com/bitcoin/bitcoin/blob/master/src/crypto/sha256.cpp)
* Potential ASIC efficiency gain ~ 1000X

The SHA algorithm is a sequence of simple math operations - additions, logical ops, and rotates.

To process a single op on a CPU or GPU requires fetching and decoding an instruction, reading data from a register file, executing the instruction, and then writing the result back to a register file.  This takes significant time and power.

A single op implemented in an ASIC takes a handful of transistors and wires.  This means every individual op takes negligible power, area, or time.  A hashing core is built by laying out the sequence of required ops.

The hashing core can execute the required sequence of ops in much less time, and using less power or area, than doing the same sequence on a CPU or GPU.  A bitcoin ASIC consists of a number of identical hashing cores and some minimal off-chip communication.

### Scrypt and NeoScrypt [Project](https://github.com/wg/scrypt)
* Potential ASIC efficiency gain ~ 1000X

Scrypt and NeoScrypt are similar to SHA in the arithmetic and bitwise operations used. Unfortunately, popular coins such as Litecoin only use a scratchpad size between 32kb and 128kb for their PoW mining algorithm. This scratch pad is small enough to trivially fit on an ASIC next to the math core. The implementation of the math core would be very similar to SHA, with similar efficiency gains.

### X16R [Project](https://github.com/todd1251/ccminer-x16r/blob/x16r/x16r/x16r.cu)
* Potential ASIC efficiency gain ~ 1000X

X16R requires the multiple hashing cores to interact through a simple sequencing state machine. Each individual core will have similar efficiency gains and the sequencing logic will take minimal power, area, or time.

The Baikal BK-X is an existing ASIC with multiple hashing cores and a programmable sequencer.  It has been upgraded to enable new algorithms that sequence the hashes in different orders.

### Equihash [Project](https://github.com/khovratovich/equihash)
* Potential ASIC efficiency gain ~ 100X

The ~150mb of state is large but possible on an ASIC. The binning, sorting, and comparing of bit strings could be implemented on an ASIC at extremely high speed.

### Cuckoo Cycle [Project](https://github.com/tromp/cuckoo)
* Potential ASIC efficiency gain ~ 100X

The amount of state required on-chip is not clear as there are Time/Memory Tradeoff attacks. A specialized graph traversal core would have similar efficiency gains to a SHA compute core.

### CryptoNight [Project](https://github.com/menekevin/cryptonight)
* Potential ASIC efficiency gain ~ 50X

Compared to Scrypt, CryptoNight does much less compute and requires a full 2mb of scratch pad (there is no known Time/Memory Tradeoff attack).  The large scratch pad will dominate the ASIC implementation and limit the number of hashing cores, limiting the absolute performance of the ASIC.  An ASIC will consist almost entirely of just on-die SRAM.

### Ethash [Project](https://github.com/ethereum/wiki/wiki/Ethash)
* Potential ASIC efficiency gain ~ 2X

Ethash requires external memory due to the large size of the DAG.  However that is all that it requires - there is minimal compute that is done on the result loaded from memory.  As a result a custom ASIC could remove most of the complexity, and power, of a GPU and be just a memory interface connected to a small compute engine.

--->

## RandoShash Algorithm Walkthrought

<!---

## Example/Testcase

--->

## Built With

* [Python](https://www.python.org/) - The Programming Language
* [PyCharm](https://www.jetbrains.com/pycharm/) - IDE
* [GitKraken](https://www.gitkraken.com/) - Github Client for Linux

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Rohan Mundhey** [Profile](https://github.com/Mundhey)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details



 
