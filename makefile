iFlags = -I/usr/local/cuda/include -I/usr/local/include/ 
cpplink =  -lcudart -lcurand -L/usr/local/cuda/lib64 -L./ -L/usr/local/cuda/lib
LINK_TARGET = kernel
OBJS =  kernel.o

ifeq ($(ConfigName),Release)
	LL = -O2 -Wall
	LG = -O2 -Xcompiler -Wall
else
	LL = -g -DDEBUG -Wall
	LG = -g -G -DDEBUG -Xcompiler -Wall
endif

all : $(LINK_TARGET)
	@echo $(ConfigName) make done

clean : 
	@rm -f $(OBJS) $(LINK_TARGET)
	@echo $(ConfigName) clean done

$(LINK_TARGET) : $(OBJS)
	g++ $(LL) -std=c++11  $(cpplink) -o  $(LINK_TARGET) $(OBJS)
 
%.o : %.cpp
	@g++ $(LL) -Wall -std=c++11 $(iFlags) -o $@ -c $<

%.o : %.c
	@g++ $(LL) -std=c++11 $(iFlags) -o $@ -c $<

%.o : %.cu
	@nvcc -arch=sm_35 $(LG) $(iFlags) -o $@ -c $<

