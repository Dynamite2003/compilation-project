# Generated from C.g4 by ANTLR 4.10
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,81,545,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,
        1,24,1,24,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,29,1,29,1,30,
        1,30,1,31,1,31,1,31,1,32,1,32,1,32,1,33,1,33,1,34,1,34,1,35,1,35,
        1,36,1,36,1,36,1,37,1,37,1,37,1,38,1,38,1,39,1,39,1,40,1,40,1,40,
        1,41,1,41,1,41,1,42,1,42,1,42,1,43,1,43,1,43,1,44,1,44,1,45,1,45,
        1,46,1,46,1,47,1,47,1,48,1,48,1,48,1,49,1,49,1,49,1,50,1,50,1,51,
        1,51,1,51,1,52,1,52,1,52,1,52,1,52,1,53,1,53,1,53,1,53,1,53,1,53,
        1,53,1,53,1,54,1,54,1,54,1,55,1,55,1,55,1,55,1,55,1,56,1,56,1,56,
        1,56,1,56,1,56,1,56,1,57,1,57,1,57,1,57,1,57,1,57,1,58,1,58,1,58,
        1,59,1,59,1,59,1,59,1,60,1,60,1,60,1,60,1,60,1,61,1,61,1,61,1,61,
        1,61,1,61,1,61,1,61,1,61,1,62,1,62,1,62,1,62,1,62,1,62,1,63,1,63,
        1,63,1,63,1,63,1,63,1,63,1,64,1,64,1,64,1,65,1,65,1,65,1,66,1,66,
        1,66,1,67,1,67,1,67,1,68,1,68,1,68,1,69,1,69,1,69,1,69,1,70,1,70,
        1,70,1,70,1,71,1,71,1,71,1,72,1,72,1,72,1,73,1,73,1,73,1,74,1,74,
        5,74,468,8,74,10,74,12,74,471,9,74,1,75,4,75,474,8,75,11,75,12,75,
        475,1,75,4,75,479,8,75,11,75,12,75,480,1,75,1,75,5,75,485,8,75,10,
        75,12,75,488,9,75,3,75,490,8,75,1,76,1,76,1,76,3,76,495,8,76,1,76,
        1,76,1,77,1,77,1,77,5,77,502,8,77,10,77,12,77,505,9,77,1,77,1,77,
        1,78,1,78,1,79,1,79,1,79,1,80,4,80,515,8,80,11,80,12,80,516,1,80,
        1,80,1,81,1,81,1,81,1,81,5,81,525,8,81,10,81,12,81,528,9,81,1,81,
        1,81,1,82,1,82,1,82,1,82,5,82,536,8,82,10,82,12,82,539,9,82,1,82,
        1,82,1,82,1,82,1,82,1,537,0,83,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,
        8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,
        19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,
        30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,
        41,83,42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,99,50,101,51,
        103,52,105,53,107,54,109,55,111,56,113,57,115,58,117,59,119,60,121,
        61,123,62,125,63,127,64,129,65,131,66,133,67,135,68,137,69,139,70,
        141,71,143,72,145,73,147,74,149,75,151,76,153,77,155,78,157,0,159,
        0,161,79,163,80,165,81,1,0,8,3,0,65,90,95,95,97,122,4,0,48,57,65,
        90,95,95,97,122,4,0,10,10,13,13,39,39,92,92,4,0,10,10,13,13,34,34,
        92,92,1,0,48,57,8,0,34,34,39,39,92,92,98,98,102,102,110,110,114,
        114,116,116,3,0,9,10,13,13,32,32,2,0,10,10,13,13,553,0,1,1,0,0,0,
        0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,
        1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,
        1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,
        1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,
        1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,
        1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,
        1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,
        1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,
        1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,
        1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,
        0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,
        0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,
        131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,
        0,0,0,141,1,0,0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,149,
        1,0,0,0,0,151,1,0,0,0,0,153,1,0,0,0,0,155,1,0,0,0,0,161,1,0,0,0,
        0,163,1,0,0,0,0,165,1,0,0,0,1,167,1,0,0,0,3,169,1,0,0,0,5,174,1,
        0,0,0,7,179,1,0,0,0,9,185,1,0,0,0,11,189,1,0,0,0,13,194,1,0,0,0,
        15,200,1,0,0,0,17,207,1,0,0,0,19,214,1,0,0,0,21,223,1,0,0,0,23,228,
        1,0,0,0,25,235,1,0,0,0,27,237,1,0,0,0,29,239,1,0,0,0,31,247,1,0,
        0,0,33,254,1,0,0,0,35,261,1,0,0,0,37,266,1,0,0,0,39,275,1,0,0,0,
        41,277,1,0,0,0,43,279,1,0,0,0,45,281,1,0,0,0,47,283,1,0,0,0,49,285,
        1,0,0,0,51,287,1,0,0,0,53,289,1,0,0,0,55,295,1,0,0,0,57,304,1,0,
        0,0,59,308,1,0,0,0,61,310,1,0,0,0,63,312,1,0,0,0,65,315,1,0,0,0,
        67,318,1,0,0,0,69,320,1,0,0,0,71,322,1,0,0,0,73,324,1,0,0,0,75,327,
        1,0,0,0,77,330,1,0,0,0,79,332,1,0,0,0,81,334,1,0,0,0,83,337,1,0,
        0,0,85,340,1,0,0,0,87,343,1,0,0,0,89,346,1,0,0,0,91,348,1,0,0,0,
        93,350,1,0,0,0,95,352,1,0,0,0,97,354,1,0,0,0,99,357,1,0,0,0,101,
        360,1,0,0,0,103,362,1,0,0,0,105,365,1,0,0,0,107,370,1,0,0,0,109,
        378,1,0,0,0,111,381,1,0,0,0,113,386,1,0,0,0,115,393,1,0,0,0,117,
        399,1,0,0,0,119,402,1,0,0,0,121,406,1,0,0,0,123,411,1,0,0,0,125,
        420,1,0,0,0,127,426,1,0,0,0,129,433,1,0,0,0,131,436,1,0,0,0,133,
        439,1,0,0,0,135,442,1,0,0,0,137,445,1,0,0,0,139,448,1,0,0,0,141,
        452,1,0,0,0,143,456,1,0,0,0,145,459,1,0,0,0,147,462,1,0,0,0,149,
        465,1,0,0,0,151,489,1,0,0,0,153,491,1,0,0,0,155,498,1,0,0,0,157,
        508,1,0,0,0,159,510,1,0,0,0,161,514,1,0,0,0,163,520,1,0,0,0,165,
        531,1,0,0,0,167,168,5,59,0,0,168,2,1,0,0,0,169,170,5,118,0,0,170,
        171,5,111,0,0,171,172,5,105,0,0,172,173,5,100,0,0,173,4,1,0,0,0,
        174,175,5,99,0,0,175,176,5,104,0,0,176,177,5,97,0,0,177,178,5,114,
        0,0,178,6,1,0,0,0,179,180,5,115,0,0,180,181,5,104,0,0,181,182,5,
        111,0,0,182,183,5,114,0,0,183,184,5,116,0,0,184,8,1,0,0,0,185,186,
        5,105,0,0,186,187,5,110,0,0,187,188,5,116,0,0,188,10,1,0,0,0,189,
        190,5,108,0,0,190,191,5,111,0,0,191,192,5,110,0,0,192,193,5,103,
        0,0,193,12,1,0,0,0,194,195,5,102,0,0,195,196,5,108,0,0,196,197,5,
        111,0,0,197,198,5,97,0,0,198,199,5,116,0,0,199,14,1,0,0,0,200,201,
        5,100,0,0,201,202,5,111,0,0,202,203,5,117,0,0,203,204,5,98,0,0,204,
        205,5,108,0,0,205,206,5,101,0,0,206,16,1,0,0,0,207,208,5,115,0,0,
        208,209,5,105,0,0,209,210,5,103,0,0,210,211,5,110,0,0,211,212,5,
        101,0,0,212,213,5,100,0,0,213,18,1,0,0,0,214,215,5,117,0,0,215,216,
        5,110,0,0,216,217,5,115,0,0,217,218,5,105,0,0,218,219,5,103,0,0,
        219,220,5,110,0,0,220,221,5,101,0,0,221,222,5,100,0,0,222,20,1,0,
        0,0,223,224,5,98,0,0,224,225,5,111,0,0,225,226,5,111,0,0,226,227,
        5,108,0,0,227,22,1,0,0,0,228,229,5,115,0,0,229,230,5,116,0,0,230,
        231,5,114,0,0,231,232,5,117,0,0,232,233,5,99,0,0,233,234,5,116,0,
        0,234,24,1,0,0,0,235,236,5,123,0,0,236,26,1,0,0,0,237,238,5,125,
        0,0,238,28,1,0,0,0,239,240,5,116,0,0,240,241,5,121,0,0,241,242,5,
        112,0,0,242,243,5,101,0,0,243,244,5,100,0,0,244,245,5,101,0,0,245,
        246,5,102,0,0,246,30,1,0,0,0,247,248,5,101,0,0,248,249,5,120,0,0,
        249,250,5,116,0,0,250,251,5,101,0,0,251,252,5,114,0,0,252,253,5,
        110,0,0,253,32,1,0,0,0,254,255,5,115,0,0,255,256,5,116,0,0,256,257,
        5,97,0,0,257,258,5,116,0,0,258,259,5,105,0,0,259,260,5,99,0,0,260,
        34,1,0,0,0,261,262,5,97,0,0,262,263,5,117,0,0,263,264,5,116,0,0,
        264,265,5,111,0,0,265,36,1,0,0,0,266,267,5,114,0,0,267,268,5,101,
        0,0,268,269,5,103,0,0,269,270,5,105,0,0,270,271,5,115,0,0,271,272,
        5,116,0,0,272,273,5,101,0,0,273,274,5,114,0,0,274,38,1,0,0,0,275,
        276,5,44,0,0,276,40,1,0,0,0,277,278,5,61,0,0,278,42,1,0,0,0,279,
        280,5,40,0,0,280,44,1,0,0,0,281,282,5,41,0,0,282,46,1,0,0,0,283,
        284,5,91,0,0,284,48,1,0,0,0,285,286,5,93,0,0,286,50,1,0,0,0,287,
        288,5,42,0,0,288,52,1,0,0,0,289,290,5,99,0,0,290,291,5,111,0,0,291,
        292,5,110,0,0,292,293,5,115,0,0,293,294,5,116,0,0,294,54,1,0,0,0,
        295,296,5,118,0,0,296,297,5,111,0,0,297,298,5,108,0,0,298,299,5,
        97,0,0,299,300,5,116,0,0,300,301,5,105,0,0,301,302,5,108,0,0,302,
        303,5,101,0,0,303,56,1,0,0,0,304,305,5,46,0,0,305,306,5,46,0,0,306,
        307,5,46,0,0,307,58,1,0,0,0,308,309,5,63,0,0,309,60,1,0,0,0,310,
        311,5,58,0,0,311,62,1,0,0,0,312,313,5,124,0,0,313,314,5,124,0,0,
        314,64,1,0,0,0,315,316,5,38,0,0,316,317,5,38,0,0,317,66,1,0,0,0,
        318,319,5,124,0,0,319,68,1,0,0,0,320,321,5,94,0,0,321,70,1,0,0,0,
        322,323,5,38,0,0,323,72,1,0,0,0,324,325,5,61,0,0,325,326,5,61,0,
        0,326,74,1,0,0,0,327,328,5,33,0,0,328,329,5,61,0,0,329,76,1,0,0,
        0,330,331,5,60,0,0,331,78,1,0,0,0,332,333,5,62,0,0,333,80,1,0,0,
        0,334,335,5,60,0,0,335,336,5,61,0,0,336,82,1,0,0,0,337,338,5,62,
        0,0,338,339,5,61,0,0,339,84,1,0,0,0,340,341,5,60,0,0,341,342,5,60,
        0,0,342,86,1,0,0,0,343,344,5,62,0,0,344,345,5,62,0,0,345,88,1,0,
        0,0,346,347,5,43,0,0,347,90,1,0,0,0,348,349,5,45,0,0,349,92,1,0,
        0,0,350,351,5,47,0,0,351,94,1,0,0,0,352,353,5,37,0,0,353,96,1,0,
        0,0,354,355,5,43,0,0,355,356,5,43,0,0,356,98,1,0,0,0,357,358,5,45,
        0,0,358,359,5,45,0,0,359,100,1,0,0,0,360,361,5,46,0,0,361,102,1,
        0,0,0,362,363,5,45,0,0,363,364,5,62,0,0,364,104,1,0,0,0,365,366,
        5,99,0,0,366,367,5,97,0,0,367,368,5,115,0,0,368,369,5,101,0,0,369,
        106,1,0,0,0,370,371,5,100,0,0,371,372,5,101,0,0,372,373,5,102,0,
        0,373,374,5,97,0,0,374,375,5,117,0,0,375,376,5,108,0,0,376,377,5,
        116,0,0,377,108,1,0,0,0,378,379,5,105,0,0,379,380,5,102,0,0,380,
        110,1,0,0,0,381,382,5,101,0,0,382,383,5,108,0,0,383,384,5,115,0,
        0,384,385,5,101,0,0,385,112,1,0,0,0,386,387,5,115,0,0,387,388,5,
        119,0,0,388,389,5,105,0,0,389,390,5,116,0,0,390,391,5,99,0,0,391,
        392,5,104,0,0,392,114,1,0,0,0,393,394,5,119,0,0,394,395,5,104,0,
        0,395,396,5,105,0,0,396,397,5,108,0,0,397,398,5,101,0,0,398,116,
        1,0,0,0,399,400,5,100,0,0,400,401,5,111,0,0,401,118,1,0,0,0,402,
        403,5,102,0,0,403,404,5,111,0,0,404,405,5,114,0,0,405,120,1,0,0,
        0,406,407,5,103,0,0,407,408,5,111,0,0,408,409,5,116,0,0,409,410,
        5,111,0,0,410,122,1,0,0,0,411,412,5,99,0,0,412,413,5,111,0,0,413,
        414,5,110,0,0,414,415,5,116,0,0,415,416,5,105,0,0,416,417,5,110,
        0,0,417,418,5,117,0,0,418,419,5,101,0,0,419,124,1,0,0,0,420,421,
        5,98,0,0,421,422,5,114,0,0,422,423,5,101,0,0,423,424,5,97,0,0,424,
        425,5,107,0,0,425,126,1,0,0,0,426,427,5,114,0,0,427,428,5,101,0,
        0,428,429,5,116,0,0,429,430,5,117,0,0,430,431,5,114,0,0,431,432,
        5,110,0,0,432,128,1,0,0,0,433,434,5,42,0,0,434,435,5,61,0,0,435,
        130,1,0,0,0,436,437,5,47,0,0,437,438,5,61,0,0,438,132,1,0,0,0,439,
        440,5,37,0,0,440,441,5,61,0,0,441,134,1,0,0,0,442,443,5,43,0,0,443,
        444,5,61,0,0,444,136,1,0,0,0,445,446,5,45,0,0,446,447,5,61,0,0,447,
        138,1,0,0,0,448,449,5,60,0,0,449,450,5,60,0,0,450,451,5,61,0,0,451,
        140,1,0,0,0,452,453,5,62,0,0,453,454,5,62,0,0,454,455,5,61,0,0,455,
        142,1,0,0,0,456,457,5,38,0,0,457,458,5,61,0,0,458,144,1,0,0,0,459,
        460,5,94,0,0,460,461,5,61,0,0,461,146,1,0,0,0,462,463,5,124,0,0,
        463,464,5,61,0,0,464,148,1,0,0,0,465,469,7,0,0,0,466,468,7,1,0,0,
        467,466,1,0,0,0,468,471,1,0,0,0,469,467,1,0,0,0,469,470,1,0,0,0,
        470,150,1,0,0,0,471,469,1,0,0,0,472,474,3,157,78,0,473,472,1,0,0,
        0,474,475,1,0,0,0,475,473,1,0,0,0,475,476,1,0,0,0,476,490,1,0,0,
        0,477,479,3,157,78,0,478,477,1,0,0,0,479,480,1,0,0,0,480,478,1,0,
        0,0,480,481,1,0,0,0,481,482,1,0,0,0,482,486,5,46,0,0,483,485,3,157,
        78,0,484,483,1,0,0,0,485,488,1,0,0,0,486,484,1,0,0,0,486,487,1,0,
        0,0,487,490,1,0,0,0,488,486,1,0,0,0,489,473,1,0,0,0,489,478,1,0,
        0,0,490,152,1,0,0,0,491,494,5,39,0,0,492,495,8,2,0,0,493,495,3,159,
        79,0,494,492,1,0,0,0,494,493,1,0,0,0,495,496,1,0,0,0,496,497,5,39,
        0,0,497,154,1,0,0,0,498,503,5,34,0,0,499,502,8,3,0,0,500,502,3,159,
        79,0,501,499,1,0,0,0,501,500,1,0,0,0,502,505,1,0,0,0,503,501,1,0,
        0,0,503,504,1,0,0,0,504,506,1,0,0,0,505,503,1,0,0,0,506,507,5,34,
        0,0,507,156,1,0,0,0,508,509,7,4,0,0,509,158,1,0,0,0,510,511,5,92,
        0,0,511,512,7,5,0,0,512,160,1,0,0,0,513,515,7,6,0,0,514,513,1,0,
        0,0,515,516,1,0,0,0,516,514,1,0,0,0,516,517,1,0,0,0,517,518,1,0,
        0,0,518,519,6,80,0,0,519,162,1,0,0,0,520,521,5,47,0,0,521,522,5,
        47,0,0,522,526,1,0,0,0,523,525,8,7,0,0,524,523,1,0,0,0,525,528,1,
        0,0,0,526,524,1,0,0,0,526,527,1,0,0,0,527,529,1,0,0,0,528,526,1,
        0,0,0,529,530,6,81,0,0,530,164,1,0,0,0,531,532,5,47,0,0,532,533,
        5,42,0,0,533,537,1,0,0,0,534,536,9,0,0,0,535,534,1,0,0,0,536,539,
        1,0,0,0,537,538,1,0,0,0,537,535,1,0,0,0,538,540,1,0,0,0,539,537,
        1,0,0,0,540,541,5,42,0,0,541,542,5,47,0,0,542,543,1,0,0,0,543,544,
        6,82,0,0,544,166,1,0,0,0,12,0,469,475,480,486,489,494,501,503,516,
        526,537,1,6,0,0
    ]

class CLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    T__50 = 51
    T__51 = 52
    T__52 = 53
    T__53 = 54
    T__54 = 55
    T__55 = 56
    T__56 = 57
    T__57 = 58
    T__58 = 59
    T__59 = 60
    T__60 = 61
    T__61 = 62
    T__62 = 63
    T__63 = 64
    T__64 = 65
    T__65 = 66
    T__66 = 67
    T__67 = 68
    T__68 = 69
    T__69 = 70
    T__70 = 71
    T__71 = 72
    T__72 = 73
    T__73 = 74
    Identifier = 75
    Constant = 76
    CharacterConstant = 77
    StringLiteral = 78
    Whitespace = 79
    LineComment = 80
    BlockComment = 81

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'void'", "'char'", "'short'", "'int'", "'long'", "'float'", 
            "'double'", "'signed'", "'unsigned'", "'bool'", "'struct'", 
            "'{'", "'}'", "'typedef'", "'extern'", "'static'", "'auto'", 
            "'register'", "','", "'='", "'('", "')'", "'['", "']'", "'*'", 
            "'const'", "'volatile'", "'...'", "'?'", "':'", "'||'", "'&&'", 
            "'|'", "'^'", "'&'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'<<'", "'>>'", "'+'", "'-'", "'/'", "'%'", "'++'", "'--'", 
            "'.'", "'->'", "'case'", "'default'", "'if'", "'else'", "'switch'", 
            "'while'", "'do'", "'for'", "'goto'", "'continue'", "'break'", 
            "'return'", "'*='", "'/='", "'%='", "'+='", "'-='", "'<<='", 
            "'>>='", "'&='", "'^='", "'|='" ]

    symbolicNames = [ "<INVALID>",
            "Identifier", "Constant", "CharacterConstant", "StringLiteral", 
            "Whitespace", "LineComment", "BlockComment" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "T__44", "T__45", "T__46", "T__47", "T__48", "T__49", 
                  "T__50", "T__51", "T__52", "T__53", "T__54", "T__55", 
                  "T__56", "T__57", "T__58", "T__59", "T__60", "T__61", 
                  "T__62", "T__63", "T__64", "T__65", "T__66", "T__67", 
                  "T__68", "T__69", "T__70", "T__71", "T__72", "T__73", 
                  "Identifier", "Constant", "CharacterConstant", "StringLiteral", 
                  "Digit", "EscapeSequence", "Whitespace", "LineComment", 
                  "BlockComment" ]

    grammarFileName = "C.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


