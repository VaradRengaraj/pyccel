from mpi4py import MPI
from numpy  import empty

from pyccel.decorators import types

# TODO: avoid declaration of integer variables 'ierr' and 'rank'
# TODO: allow access to process rank through property 'comm.rank'
# TODO: allow passing MPI communicator to functions
# TODO: understand that 'recvbuf' has intent(inout)

#==============================================================================

@types( 'int[:]', 'int[:]' )
def np_allreduce( sendbuf, recvbuf ):

    comm = MPI.COMM_WORLD
    ierr = -1
    recvbuf[:] = 0

    comm.Allreduce( sendbuf, recvbuf, MPI.SUM )

# ...
@types( 'int[:]', int )
def np_bcast( buf, root ): 

    comm = MPI.COMM_WORLD
    ierr = -1
    rank = -1
    rank = comm.Get_rank()

    if rank != root:
        buf[:] = 0

    comm.Bcast( buf, root )
