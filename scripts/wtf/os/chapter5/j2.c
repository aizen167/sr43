#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <sys/wait.h>

int
main(int argc, char *argv[])
{
	close(STDOUT_FILENO);
	int fd = open("./j2.output",O_CREAT|O_WRONLY|O_TRUNC,S_IRWXU);
	int rc = fork();
	if (rc <0) {			// fork failed; exit
		fprintf(stderr, "fork failed\n");
		exit(1);
	} else if (rc ==0) {	//child: redirect standard output to a file
		//now exec "wc"...
		printf("fd===%d\n", fd);
		char *myargs[3];
		myargs[0] = strdup("wc");	// program: "wc" (word count)
		myargs[1] = strdup("j2.c");	// argument: file to count
		myargs[2] = NULL;			// marks end of array
		execvp(myargs[0], myargs);	// runs word count
	} else {				//parent goes down this path (main)
		//now exec "wc"...
		char *myargs[3];
		myargs[0] = strdup("wc");	// program: "wc" (word count)
		myargs[1] = strdup("j2.c");	// argument: file to count
		myargs[2] = NULL;			// marks end of array
		execvp(myargs[0], myargs);	// runs word count
	}
	return 0;
}
