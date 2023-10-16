from collections import namedtuple

Genotype = namedtuple('Genotype', 'normal normal_concat reduce reduce_concat')

PRIMITIVES = [
    'none',
    'max_pool_3x3',
    'avg_pool_3x3',
    'skip_connect',
    'sep_conv_3x3',
    'sep_conv_5x5',
    'dil_conv_3x3',
    'dil_conv_5x5'
]

NASNet = Genotype(
  normal = [
    ('sep_conv_5x5', 1),
    ('sep_conv_3x3', 0),
    ('sep_conv_5x5', 0),
    ('sep_conv_3x3', 0),
    ('avg_pool_3x3', 1),
    ('skip_connect', 0),
    ('avg_pool_3x3', 0),
    ('avg_pool_3x3', 0),
    ('sep_conv_3x3', 1),
    ('skip_connect', 1),
  ],
  normal_concat = [2, 3, 4, 5, 6],
  reduce = [
    ('sep_conv_5x5', 1),
    ('sep_conv_7x7', 0),
    ('max_pool_3x3', 1),
    ('sep_conv_7x7', 0),
    ('avg_pool_3x3', 1),
    ('sep_conv_5x5', 0),
    ('skip_connect', 3),
    ('avg_pool_3x3', 2),
    ('sep_conv_3x3', 2),
    ('max_pool_3x3', 1),
  ],
  reduce_concat = [4, 5, 6],
)
    
AmoebaNet = Genotype(
  normal = [
    ('avg_pool_3x3', 0),
    ('max_pool_3x3', 1),
    ('sep_conv_3x3', 0),
    ('sep_conv_5x5', 2),
    ('sep_conv_3x3', 0),
    ('avg_pool_3x3', 3),
    ('sep_conv_3x3', 1),
    ('skip_connect', 1),
    ('skip_connect', 0),
    ('avg_pool_3x3', 1),
    ],
  normal_concat = [4, 5, 6],
  reduce = [
    ('avg_pool_3x3', 0),
    ('sep_conv_3x3', 1),
    ('max_pool_3x3', 0),
    ('sep_conv_7x7', 2),
    ('sep_conv_7x7', 0),
    ('avg_pool_3x3', 1),
    ('max_pool_3x3', 0),
    ('max_pool_3x3', 1),
    ('conv_7x1_1x7', 0),
    ('sep_conv_3x3', 5),
  ],
  reduce_concat = [3, 4, 6]
)

DARTS_V1 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 0), ('sep_conv_3x3', 1), ('skip_connect', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 2)], normal_concat=[2, 3, 4, 5], reduce=[('max_pool_3x3', 0), ('max_pool_3x3', 1), ('skip_connect', 2), ('max_pool_3x3', 0), ('max_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 2), ('avg_pool_3x3', 0)], reduce_concat=[2, 3, 4, 5])
DARTS_V2 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('skip_connect', 0), ('skip_connect', 0), ('dil_conv_3x3', 2)], normal_concat=[2, 3, 4, 5], reduce=[('max_pool_3x3', 0), ('max_pool_3x3', 1), ('skip_connect', 2), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 2), ('max_pool_3x3', 1)], reduce_concat=[2, 3, 4, 5])

# eval-EXP-20211204-074723
DARTS_V3 = Genotype(normal=[('dil_conv_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 1), ('sep_conv_3x3', 1),('skip_connect', 0), ('sep_conv_3x3', 0), ('dil_conv_3x3', 2)], normal_concat=[2, 3, 4, 5],reduce=[('skip_connect', 0), ('avg_pool_3x3', 1), ('skip_connect', 2), ('skip_connect', 1), ('max_pool_3x3', 0), ('avg_pool_3x3', 2), ('max_pool_3x3', 2), ('max_pool_3x3', 1)], reduce_concat=[2, 3, 4, 5])
PDARTS = Genotype(normal=[('skip_connect', 0), ('dil_conv_3x3', 1), ('skip_connect', 0),('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 3), ('sep_conv_3x3',0), ('dil_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 0), ('dil_conv_5x5', 2), ('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('dil_conv_3x3', 1), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
PC_DARTS_cifar = Genotype(normal=[('sep_conv_3x3', 1), ('skip_connect', 0), ('sep_conv_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 1), ('avg_pool_3x3', 0), ('dil_conv_3x3', 1)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 1), ('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), ('sep_conv_3x3', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))
PC_DARTS_image = Genotype(normal=[('skip_connect', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('skip_connect', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 3), ('sep_conv_3x3', 1), ('dil_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('skip_connect', 1), ('dil_conv_5x5', 2), ('max_pool_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))



RACL = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('skip_connect', 1), ('sep_conv_3x3', 0), ('skip_connect', 3), ('sep_conv_3x3', 3), ('skip_connect', 4)], normal_concat=[2, 3, 4, 5], reduce=[('sep_conv_3x3',0), ('sep_conv_5x5', 1), ('avg_pool_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_5x5',1), ('sep_conv_3x3', 2), ('dil_conv_3x3', 3)], reduce_concat=[2, 3, 4, 5])
ADVRUSH = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_5x5', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 0), ('sep_conv_3x3', 1)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('skip_connect', 0), ('dil_conv_3x3', 2), ('skip_connect', 0), ('avg_pool_3x3', 1), ('skip_connect', 0), ('skip_connect', 2)], reduce_concat=range(2, 6))


# Random
ES_CRA_ME_random = Genotype(normal=[('sep_conv_5x5', 1), ('sep_conv_5x5', 1), ('sep_conv_3x3', 2), ('dil_conv_3x3', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('dil_conv_3x3', 3), ('avg_pool_3x3', 4)], normal_concat=[2,3,4,5], reduce=[('avg_pool_3x3', 1), ('dil_conv_5x5', 1), ('skip_connect', 1), ('dil_conv_3x3', 1), ('dil_conv_3x3', 3), ('dil_conv_5x5', 2), ('dil_conv_5x5', 4), ('dil_conv_3x3', 4)], reduce_concat=[2,3,4,5])


# ES-CRA-ME
ES_CRA_ME_10 = Genotype(
  normal=[
    ('dil_conv_5x5', 0),
    ('sep_conv_3x3', 0),
    ('dil_conv_5x5', 1),
    ('dil_conv_3x3', 1),
    ('dil_conv_5x5', 3),
    ('dil_conv_3x3', 0),
    ('dil_conv_5x5', 2),
    ('dil_conv_3x3', 0)],
  normal_concat=range(2, 6),
  reduce=[
    ('avg_pool_3x3', 0),
    ('sep_conv_5x5', 1),
    ('dil_conv_5x5', 2),
    ('sep_conv_5x5', 0),
    ('sep_conv_3x3', 3),
    ('skip_connect', 1),
    ('sep_conv_5x5', 4),
    ('dil_conv_5x5', 0)],
  reduce_concat=range(2, 6))


ES_CRA_ME_100 = Genotype(normal=[('sep_conv_5x5', 1), ('dil_conv_3x3', 0), ('sep_conv_3x3', 1), ('skip_connect', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 2), ('avg_pool_3x3', 0), ('dil_conv_3x3', 1)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 1), ('sep_conv_5x5', 0), ('max_pool_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('sep_conv_5x5', 3), ('sep_conv_3x3', 1), ('sep_conv_5x5', 2)], reduce_concat=range(2, 6))