# ML for Encrypted Traffic Classification
### Introduction
<pre>
This tool uses machine learning to analyse encrypted network traffic for maliciious activity without the need to decrypt packets. 

This project was largely influenced by <a href = "https://resources.sei.cmu.edu/asset_files/Presentation/2016_017_001_450411.pdf">Cisco research</a> from 2016.
</pre>
### Dependencies
- Python
  - scikit-learn
  - numpy
  - pandas
  - imblearn
- Linux 
- Joy

#### Joy
[Joy](https://github.com/cisco/joy) is a BSD-licensed libpcap-based software package for extracting data features from live network traffic or packet capture (pcap) files, using a flow-oriented model similar to that of IPFIX or Netflow, and then representing these data features in JSON.

#### Setting up Joy
1. Install Joy dependencies:

       [sudo] apt-get update
      
       [sudo] apt-get install gcc git libcurl3 libcurl4-openssl-dev libpcap0.8 libpcap-dev libssl-dev make python python-pip ruby ruby-ffi libz-dev
      
2. Download Joy:
    
       git clone https://github.com/cisco/joy.git
       cd joy

3.  Configure:

        ./configure --enable-gzip
       
4.  Build:
      
        make clean; make

5.  Installation:
  
        sudo ./install_joy/install-sh   
    
### How It Works
It takes as input, packet capture files. These files are fed into Joy to extract JSON formatted features including TLS metadata, DNS, HTTP, Netflow, etc depending on the argument passed to "bin/joy ...".

The JSON data is further parsed to extract TLS metadata information as input features to our model.
These features can broadly be categoried as:
1. TLS/SSL Handshake Information:
  - Ciphersuites
  - Extensions
  - Key length
  - Server Certificate
2. Byte Distribution
3. Individual Flow Metadata
4. Netflow Information
