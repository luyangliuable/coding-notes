#include <sgx_urts.h>
#include <stdio.h>

sgx_status_t enclave_print_hello_world(sgx_enclave_id_t eid) {
  sgx_status_t ret = SGX_ERROR_UNEXPECTED;

  ret = ecall_print_hello_world(eid);

  return ret;
}
