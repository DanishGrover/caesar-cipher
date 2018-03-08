INTRODUCTION
Security is one of the important aspects in computing. In data transfer, security must be considered as one of the method implemented to ensure secure data transfer. Data transfer is transferring information from a location or host to another host, or server. To have a secure data transfer, few method can be applied, and one of them is encryption of data, prepare it to be transferred in encrypted way and decrypted when the data want to be used.

 As the importance and the value of exchanged data over the Internet or other media types are increasing, the search for the best solution to offer the necessary protection against the data thieves' attacks along with providing these services under timely manner is one of the most active subjects in the security related communities. The primary goal of any system is that the data cannot be modified by any external user or intruder. To avoid such a type of situation convert data into a non readable form at sender side and convert that data in readable form again at receiver side. The technique and science of creating non readable data or cipher so that only authorized person is only able to read the data is called Cryptograph. It is the art and science of protecting information from undesirable individuals by converting it into a form non-recognizable by its attackers while stored and transmitted.
 In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

SOFTWARE AND HARDWARE REQUIREMENT SPECIFICATION

Technology Used:  Python
IDE:  Python IDLE 3.X

METHODOLOGY

Cryptanalysis is the art of breaking codes and ciphers. The Caesar cipher is probably the easiest of all ciphers to break. Since the shift has to be a number between 1 and 25, (0 or 26 would result in an unchanged plaintext) we can simply try each possibility and see which one results in a piece of readable text. If you happen to know what a piece of the cipher text is, or you can guess a piece, then this will allow you to immediately find the key.

If this is not possible, a more systematic approach is to calculate the frequency distribution of the letters in the cipher text. This consists of counting how many times each letter appears. Natural English text has a very distinct distribution that can be used help crack codes.


