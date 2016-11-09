/*******************************************************************/
/*     filename : pso_quality.h                                    */
/*     date     : 2012.10.03                                       */
/*******************************************************************/

#ifndef PSO_QUALITY_H
#define PSO_QUALITY_H
/////////////////////////////////////////////////////////////////////
double   fitness(double *x, int dim) ; /* �A���禡                 */

double** Allocate2Dim(int m, int n);   /* �t�mdouble arr[m][n]     */
void     Release2Dim(double** ptr);    /* ����G���O����           */
double*  Allocate1Dim(int x);          /* �t�mdouble arr[x]        */
void     Release1Dim(double* ptr);     /* ����@���O����           */

void   SetParam(                       /* �]�mPSO �Ѽ�,�t�m�O����  */
                 double w,             /* �ۨ��v���Ѽ�w            */
                 double c1,            /* �g��`��c1               */
                 double c2,            /* ����g��`��c2           */
                 unsigned dim,         /* �ѪŶ�������             */   
                 unsigned particle_cnt /* �ɤl�Ӽ�                 */
               );

void   SetSolRange(                    /* �]�w�ѪŶ�����           */
                    double* min_pos,   /* �ѪŶ��̤p����           */
                    double* max_pos,   /* �ѪŶ��̤j����           */
                    double* max_v      /* �ɤl���ʳ̤j�t�׭���     */
                  );

void ParticleInit();                   /* �ɤl�s��l��             */
void ParticleSwarm();                  /* �U�ɤl�}�l����           */
void ParticleDisplay();                /* ��ܲɤl�ԲӸ�T         */

void GetOptimzation(                   /* ���o���u��               */
                     double* x,        /* ���u����                 */
                     double* fitv      /* ���u�Ѥ��A����           */
					);            

void ParticleRelease();                /* �ɤl����O����           */ 
/////////////////////////////////////////////////////////////////////
#endif
