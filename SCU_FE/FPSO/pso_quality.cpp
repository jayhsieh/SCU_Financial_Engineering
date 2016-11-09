/*******************************************************************/
/*     filename : pso_quality.cpp                                  */
/*     date     : 2012.10.03									   */
/*******************************************************************/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include "pso_quality.h"

//////////////////////////////////////////////////////////////////////////
//  macro �]�w
/* ����[0,1] �ü�*/
// #define RND() ((double) ((rand()<<15)|rand() )/( (RAND_MAX << 15) | RAND_MAX)) 
#define RND() ((double)rand()/RAND_MAX )
/* ����[low,up] �ü�*/
#define random(low, up) ( ((up)-(low)) * RND()  + (low) )
/* ����[-1,1] �ü�*/
#define RND1() (random(-1.0, 1.0)) 
//////////////////////////////////////////////////////////////////////////
// �R�A�ܼ�

static double w;
static double c1;
static double c2;

static unsigned  pcnt;         /* �ɤl�s�Ӽ�                       */
static unsigned  dim;          /* �ѪŶ�����                       */

static double **particle_pos;  /* �U�ɤl�ثe��m[pcnt][dim]         */
static double **particle_v;    /* �U�ɤl�ثe�t��[pcnt][dim]         */
static double  *particle_fv;   /* �U�ɤl�ثe�A����[pcnt]            */
static double **pbest_pos;     /* �U�ɤl�ثe���̨Φ�m[pcnt][dim] */
static double  *pbest_fv ;     /* �U�ɤl�ثe�̨ξA����[pcnt]        */

static double  *gbest_pos;     /* ����ثe���̨Φ�m[dim]         */
static double   gbest_fv;      /* ����ثe�̨ξA����               */
static double *max_pos;        /* �U���פ��̤j��[dim]               */
static double *min_pos;        /* �U���פ��̤p��[dim]               */
static double *max_v  ;        /* �U���׳̤j�t�׭���[dim]           */

void ParticleDisplay()
{
     int i, j;
     for(i=0; i!=pcnt; ++i){
           for(j=0; j!=dim; ++j)
                printf("%+6.3lf(%+6.3lf) ", particle_pos[i][j],  particle_v[i][j]);
           printf("[%+10.5lf]\n",particle_fv[i]);
     }
}

//////////////////////////////////////////////////////////////////////////
// ------------------------------------------------------------------
// ******************************************************************
// �A���禡, De Jong, Goldberg
double fitness(double *x, int dim)
{
     int i;
     double SinMult=1.0, mult=1.0;

     for(i=0; i!=dim; ++i)
	 {
           mult*=x[i];
           SinMult*=sin(x[i]);
     }
     return sqrt(fabs(mult))*SinMult;
	 
}
// ******************************************************************
// ------------------------------------------------------------------
// �t�m�G���O����double arr[m][n]
double** Allocate2Dim(int m, int n)
{
     int i;
     double *trunk = (double*)malloc(sizeof(double)*m*n);
     double **p = (double**)malloc(sizeof(double*)*m);
     for(i=0; i<m; ++i){
           p[i]= trunk;
           trunk+=n;
     }
     return p;
}
// ------------------------------------------------------------------
// ����G���O����
void Release2Dim(double **ptr)
{
     free(*ptr), free(ptr);
}

// ------------------------------------------------------------------
// �t�m�@���O����double arr[x]
double*  Allocate1Dim(int x)
{
     return (double*)malloc(sizeof(double)*x);
}
// ------------------------------------------------------------------
// �t�m�@���O����
void Release1Dim(double* ptr)
{
     free(ptr);
}
// ------------------------------------------------------------------
// �]�mpso �����Ѽ�
void   SetParam( double _w,             /* �ۨ��v���Ѽ�w         */
                 double _c1,            /* �g��`��c1            */
                 double _c2,            /* ����g��`��c2        */
                 unsigned _dim,         /* �ѪŶ�������          */   
                 unsigned _particle_cnt /* �ɤl�Ӽ�              */
               )
{
     w=_w, c1=_c1, c2=_c2;
     dim=_dim, pcnt=_particle_cnt;

     // �t�m�����O����Ŷ�
     particle_pos = Allocate2Dim(pcnt, dim); /* �U�ɤl�ثe��m        */
     particle_v   = Allocate2Dim(pcnt, dim); /* �U�ɤl�ثe�t��        */
     particle_fv  = Allocate1Dim(pcnt);      /* �U�ɤl�ثe�A����      */
     pbest_pos    = Allocate2Dim(pcnt, dim); /* �U�ɤl�ثe���̨Φ�m*/
     pbest_fv     = Allocate1Dim(pcnt);      /* �U�ɤl�ثe�̨ξA����  */
     gbest_pos    = Allocate1Dim(dim);       /* ����ثe���̨Φ�m  */
     max_pos      = Allocate1Dim(dim);       /* �U���פ��̤j��        */
     min_pos      = Allocate1Dim(dim);       /* �U���פ��̤p��        */
     max_v        = Allocate1Dim(dim);       /* �U���׳̤j�t�׭���    */
}

// ------------------------------------------------------------------
// �]�mpso �ѪŶ������Ѽ�
void   SetSolRange(						/* �]�w�ѪŶ�����        */
                    double* _min_pos,   /* �ѪŶ��̤p����        */
                    double* _max_pos,   /* �ѪŶ��̤j����        */
                    double* _max_v      /* �ɤl���ʳ̤j�t�׭���  */
                  )
{
     memcpy( (void*)min_pos, (void*)_min_pos, dim*sizeof(double));
     memcpy( (void*)max_pos, (void*)_max_pos, dim*sizeof(double));
     memcpy( (void*)max_v  , (void*)_max_v  , dim*sizeof(double));
}
// ------------------------------------------------------------------
// �ɤl�s��l��
void ParticleInit()
{
     int i, j;

     srand((unsigned)time(NULL));
     for(i=0; i!=pcnt; ++i){
           for(j=0; j!=dim; ++j){
                /* �H�����ͦU�ɤl��m*/
                particle_pos[i][j] = random(min_pos[j], max_pos[j]);
                /* �H�����ͦU�ɤl�t��*/
                particle_v[i][j]   = random(0.0, max_v[j]);
           }
           /* �p��U�ɤl�A����*/
           pbest_fv[i]=particle_fv[i] = fitness(particle_pos[i], dim);

           /* ��s����̨θ�*/
           if(i==0 || pbest_fv[i] > gbest_fv) {
                memcpy((void*)gbest_pos, (void*)pbest_pos[i], sizeof(double)*dim);
                gbest_fv = pbest_fv[i];
           }          
     }
}
// ------------------------------------------------------------------
// �U�ɤl�}�l����
void ParticleSwarm()
{
     int i, j;
     double tmp;
     
     for(i=0; i!=pcnt; ++i){
           for(j=0; j!=dim; ++j){
                /* ��s�U�ɤl�t��*/
                particle_v[i][j] = \
                     w * particle_v[i][j] + \
                     c1 * RND1() * (pbest_pos[i][j]-particle_pos[i][j]) + \
                     c2 * RND1() * (gbest_pos[j]   -particle_pos[i][j]) ;

                /* �P�_�t�׬O�_�W�L�W�U��*/
                if(particle_v[i][j] > max_v[j]  ||
                     particle_v[i][j] < -max_v[j]) /* ���s���ͤ@�t��*/
                     particle_v[i][j] = random(0.0, max_v[j]);

                /* ��s�U�ɤl��m*/
                particle_pos[i][j] += particle_v[i][j];

                /* �W�L�W�U�ɡA���s���ͤ@�s��m*/
                if(particle_pos[i][j] > max_pos[j] ||
                     particle_pos[i][j] < min_pos[j]
                     )
                     particle_pos[i][j] = random(min_pos[j], max_pos[j]);
           }
         /* ��s�U�ɤl�A����*/
           tmp = particle_fv[i] = fitness(particle_pos[i], dim);
           /* ��s�U�ɤl�̨ξA����*/
           if(tmp > pbest_fv[i]) {
                pbest_fv[i] = tmp;
                memcpy((void*)pbest_pos[i], (void*)particle_pos[i], sizeof(double)*dim);
           }
           /* ��s����̨ξA���� */
           if(tmp > gbest_fv) {
                gbest_fv = tmp;
                memcpy((void*)gbest_pos, (void*)particle_pos[i], sizeof(double)*dim);
           }
     }
}

// ------------------------------------------------------------------
// ���o���u��
void GetOptimzation(double *x, double *fitv)
{
     memcpy((void*)x, (void*)gbest_pos, sizeof(double)*dim);
     *fitv = gbest_fv;
}
// ------------------------------------------------------------------
// �ɤl����O����
void ParticleRelease()
{
     Release2Dim(particle_pos);
     Release2Dim(particle_v);
     Release1Dim(particle_fv);
     Release2Dim(pbest_pos);
     Release1Dim(pbest_fv);
     Release1Dim(gbest_pos);
     Release1Dim(max_pos);
     Release1Dim(min_pos);
}                    
//////////////////////////////////////////////////////////////////////////
