%module mucal

%{
#define SWIG_FILE_WITH_INIT
#include "mucal.h"
%}

int name_z(char *name);
int mucal(char *name, int ZZ, double ephot, char unit, int pflag,
	  double *energy, double *xsec, double *fluo, char *errmsg);