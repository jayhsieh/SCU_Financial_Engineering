/*******************************************************************/
/*     filename : Fixed Paticle Swarm Optimization (FPSO)          */
/*     date     : 2012.10.03                                       */
/*******************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "pso_quality.h"

#define W        0.9		/* �ۨ��v���Ѽ�	*/
#define C1       2.0		/* �g��`��     */
#define C2       2.0		/* ����g��`�� */
#define DIM      2          /* ����			*/
#define PCNT     30         /* �ɤl��		*/
#define ITERATOR 10000      /* ���N����		*/

void main(void)
{
	unsigned i = ITERATOR;
    double  best_fv;                        /* �̨ξA����*/		//Max or Min �ؼШ�ƭ�
    double  *min_pos = Allocate1Dim(DIM);  	/* ���׳̤p��*/		//�t�m�@���O����double arr[x]
    double  *max_pos = Allocate1Dim(DIM);  	/* ���׳̤j��*/		//�t�m�@���O����double arr[x]
    double  *best_pos = Allocate1Dim(DIM);  /* ���׳̨έ�*/		//�t�m�@���O����double arr[x]
    double  *max_v = Allocate1Dim(DIM);  	/* �t�׭���  */		//�t�m�@���O����double arr[x]
	clock_t t1, t2;
	t1 = clock();							//�p�ɶ}�l
	
// ----------------------------------------------------
    // �]�w�Ѽ�
    min_pos[0]=0.0   , max_pos[0]=10.0;
    min_pos[1]=0.0   , max_pos[1]=10.0;

    max_v[0] = 0.0006 * ( max_pos[0] - min_pos[0] );
    max_v[1] = 0.0006 * ( max_pos[1] - min_pos[1] );     

    SetParam(W, C1, C2, DIM, PCNT);			// �]�mpso �����Ѽ�
    SetSolRange(min_pos, max_pos, max_v);	// �]�mpso �ѪŶ������Ѽ�
     
    //----------------------------------------------------
    //�}�l�i��pso algorithm
     
    ParticleInit();                       	/* ��l�Ƴ]�w      */	// �ɤl�s��l��
    while(i--)                            	/* �}�l�i�歡�N    */
		ParticleSwarm();                	/* �ɤl���ʻP��s  */	// �U�ɤl�}�l����
    GetOptimzation(best_pos, &best_fv);   	/* ���o�̨έ�      */	// ���o���u��

		for(i=0; i!=DIM; ++i)
			printf("#x%u = %10.7lf\n", i+1, best_pos[i]);

    printf("find best fitness : %.16e\n", best_fv);

	t2 = clock();							//�p�ɵ���
    printf("--- Total CPU time = %lf ---\n", (t2-t1)/(double)(CLOCKS_PER_SEC));
	system("pause");
    //----------------------------------------------------
    //�̫�����O����
    ParticleRelease();
    Release1Dim(min_pos);
    Release1Dim(max_pos);
    Release1Dim(best_pos);
}
