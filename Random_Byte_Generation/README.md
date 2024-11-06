# Random Byte Generation Task
### This script generates two large random byte files to illustrate the difference between cryptographically secure and insecure random generation methods.

## Overview
Cryptographic Randomness: Generated using secrets.token_bytes, suitable for secure contexts.
Weak Randomness: Generated using a custom weak_rng function with random.randbytes, not suitable for cryptographic purposes.
Process
Generate 4 GB of Random Data: Creates two data sets, one secure and one weak.
Randomly Assign Data to Files:
Based on a random choice, challenge.bin is assigned either the secure or weak bytes.
The other data set is stored in other.bin.
Log the Assignment: answer.txt records which data type was assigned to challenge.bin.
## Output Files
challenge.bin: Contains either secure or weak random data.
other.bin: Contains the other type of random data.
answer.txt: Notes the type of data in challenge.bin:
"Random world": challenge.bin has secure data.
"Weak PRNG world": challenge.bin has weak data.

## Usage
### Run: 
```bash
python random_generator.py
```
