
# E-Voting System Using Visual Cryptography

## Overview

This project implements a secure **E-Voting System** utilizing **Visual Cryptography**. The primary goal is to ensure a secure and confidential voting process by encrypting voter ballots into cryptographic shares and only allowing reconstruction when the correct shares are combined. This project uses client-server architecture to transmit cryptographic shares between users and the server, ensuring secure communication and vote validation.

### Problem Statement

In an electronic voting system, security and privacy are of utmost importance. Traditional voting systems can be susceptible to tampering and unauthorized access. Visual cryptography provides a secure solution by dividing the vote (image of the vote or ballot) into multiple encrypted shares. The original vote can only be reconstructed when all shares are combined, ensuring that no intermediary can access the vote without full control over all the shares.

### How We Are Solving It

Our system encrypts each vote into two or more cryptographic shares. These shares are distributed among the server and the voters (clients). Only when the correct number of shares is combined can the original vote be reconstructed, making the system highly secure and resistant to unauthorized access.

- **Client Side**: Voters use a graphical interface to input their details, cast their vote, and encrypt it using visual cryptography. The cryptographic shares are generated on the client-side and sent to the server.
- **Server Side**: The server collects cryptographic shares and ensures they are stored securely. Once voting is complete, the server combines the shares to reconstruct the votes and tally the results.
- **Database**: The system uses an SQLite database to store voter details, votes (in encrypted form), and email addresses for validation.

## Requirements

### Python Packages

- `Pillow` (for image processing and manipulation)
- `tkinter` (for building the graphical interface for voters)
- `socket` (for communication between the client and server)
- `sqlite3` (for storing voter and vote information)
- `validate_email` (for validating voter email addresses)
- `cryptography` (for managing encryption and decryption functions)

You can install the required dependencies using the following command:

```bash
pip install Pillow validate_email cryptography
```

### Additional Requirements

- A valid **TrueType font (TTF)** for image generation.
- Ensure the **server** is running before starting the client application.

## Application Workflow

1. **Client Application**:
   - The voter inputs their email address and cast their vote via the user interface.
   - The vote is split into cryptographic shares.
   - These shares are transmitted to the server via a secure socket connection.
   - The client ensures that only authorized users (validated via email) can cast their vote.

2. **Server Application**:
   - The server listens for incoming connections from clients.
   - Once it receives the cryptographic shares, it stores them in an SQLite database.
   - The server reconstructs the votes once voting is complete and tallies the results.

3. **Database**:
   - An **SQLite** database (`elections_results.db`) is used to store:
     - Voter email addresses for validation.
     - Cryptographic shares of the votes.
     - Voting results after combining the cryptographic shares.
   - The database is updated as votes are cast and shares are received.

## Results and Vote Reconstruction

Once voting is completed, the server collects the cryptographic shares from all voters. It uses these shares to reconstruct the original votes. The results are securely stored in the SQLite database, and the final tally of votes can be accessed by authorized personnel.

The following steps are involved in reconstructing the votes:

1. Combine the cryptographic shares stored in the database.
2. Recreate the original votes from the shares.
3. Store the voting results for further processing.

## How to Run the System

### 1. Start the Server

Run the server to start listening for client connections and handle incoming votes.

```bash
python Server.py
```

### 2. Start the Client

Voters use the client-side application to cast their votes, which are encrypted and transmitted to the server.

```bash
python Client.py
```

### 3. View Results

Once all votes are cast, the server reconstructs the votes from the cryptographic shares and stores the results in the database.

## Project Structure

```bash
├── Client.py        # Client-side voting application with Tkinter interface
├── Server.py        # Server-side application for handling connections and vote tallying
├── crypto.py        # Cryptographic functions for image processing and vote encryption
├── elections_results.db   # SQLite database for storing voter details and encrypted shares
└── README.md        # Project documentation
```

## Conclusion

This project demonstrates the use of visual cryptography to build a secure e-voting system. By splitting votes into encrypted shares and reconstructing them only with full access to all shares, we ensure the confidentiality and security of the voting process. This system is resistant to tampering, unauthorized access, and provides a safe mechanism for tallying votes.

## License

This project is licensed under the MIT License.
