# APPIOT2024 Lab 3: Exploring AMQP

This repository contains example scripts for the Advanced Message Queuing Protocol (AMQP) lab session part of the APPIOT2024 course. These scripts are designed to help students gain practical experience with AMQP through hands-on exercises.

## Repository Contents

- `proton_receiver.py`: Script demonstrating how to receive messages over AMQP using Qpid Proton API (AMQP 1.0 client library for Python).
- `proton_sender.py`: Script for sending messages over AMQP using Qpid Proton API (AMQP 1.0 client library for Python).
- `pika_receiver.py`: Script demonstrating how to receive messages over AMQP using Pika (RabbitMQ AMQP 0-9-1 client library for Python)
- `pika_sender.py`: Script for sending messages over AMQP using Pika (RabbitMQ AMQP 0-9-1 client library for Python)

## Getting Started

To use these scripts, clone this repository to your local machine. Make sure to have a RabbitMQ server running as per the lab instructions provided on Moodle.

## Note

Detailed instructions, including how to set up your environment, run each script, and complete the lab exercises, are available on the course's Moodle page.

## License

The code provided in this repository is derived from examples found in the respective libraries' official repositories. The license for each code example follows the license outlined by its respective library. For detailed licensing information, please refer to the original libraries' repositories:

- For AMQP scripts:
  - [Apache Qpid Proton repository](https://github.com/apache/qpid-proton)
  - [Pika repository](https://github.com/pika/pika)

## References

This repository contains example scripts inspired by and adapted from the following sources:

- AMQP examples were adapted from:
  - Apache Qpid Proton documentation and examples.
  - Pika documentation and examples.

These scripts are intended for educational purposes within the EURECOM APPIOT 2024 course to facilitate understanding of the AMQP and XMPP protocols.
