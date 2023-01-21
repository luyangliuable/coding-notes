# Intel Software Guard Extensions

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Intel Software Guard Extensions](#intel-software-guard-extensions)
    - [SGX Enclave](#sgx-enclave)
        - [Trusted Section](#trusted-section)
        - [Untrusted Section](#untrusted-section)
        - [Ecall and Ocall functions](#ecall-and-ocall-functions)
            - [Example](#example)
    - [Source](#source)

<!-- markdown-toc end -->


## SGX Enclave
In an SGX enclave, the code and data are divided into two sections: the trusted and the untrusted sections.

### Trusted Section
The trusted section contains the code and data that are protected by the enclave and that have access to the sensitive data and functionality provided by the enclave. This section includes the main logic of the application, such as cryptographic operations, data processing, and any other functionality that needs to be protected from the untrusted host.

### Untrusted Section
The untrusted section contains the code and data that are not protected by the enclave and that have limited access to the sensitive data and functionality provided by the enclave. This section includes the code that communicates with the host, such as the EDL functions that are called by the host, the code that manages the enclave's lifecycle, such as the code that creates and destroys the enclave, and any other code that does not need to be protected by the enclave.

### Ecall and Ocall functions
The trusted and untrusted sections are separated by the use of the ecall and ocall functions.

* ecall (enclave call) functions are functions that are **executed inside the enclave and that can be called from the untrusted host**. These functions are defined in the untrusted section and are used to invoke the functionality provided by the enclave.

* ocall (outside call) functions are functions that are **executed outside the enclave and that can be called from the trusted section**. These functions are used to perform operations that are not available inside the enclave, such as accessing the file system or making network connections.

* The trusted section should include the main logic of the application and it should only perform the operations that need to be protected by the enclave

* The untrusted section should include the code that communicates with the host and the code that manages the enclave's lifecycle. It should also **include the EDL functions** that are called by the host.

#### Example

```edl
enclave {
    trusted {
        public void ecall_hello_world([in, string], const char *str);
    };

    untrusted {
        void ocall_print_string([in, string] const char *str);
    };
}
```


## Source

* https://www.youtube.com/watch?v=3MDIPAZnSTw