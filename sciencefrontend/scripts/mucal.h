/* mucal.h
 *   public interface for mucal.c
 *   boyan boyanov 2/95
 */

#ifndef MUCAL_H
#define MUCAL_H

/* the return codes for mucal */
enum {
  no_error = 0,        /* no error */
  no_input,            /* no name, no Z, no service */
  no_zmatch,           /* Z does not match name */
  no_data,             /* data not avaialble for requested material */
  bad_z,               /* bad Z given as input */
  bad_name,            /* invalid element name */
  bad_energy,          /* negative photon energy */
  within_edge,         /* photon energy within 1 eV of an edge */
  m_edge_warn,         /* M-edge data for a Z<30 element requested */
  satan_rules=666      /* internal error of dubious origin :-) */
};

int name_z(char *name);
int mucal(char *name, int ZZ, double ephot, char unit, int pflag,
	  double *energy, double *xsec, double *fluo, char *errmsg);

#endif /* MUCAL_H */
