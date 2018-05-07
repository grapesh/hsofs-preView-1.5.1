#!/bin/bash

## Load Python 2.7.13
#module use /usrx/local/dev/modulefiles
#module load python/2.7.13

export pyPath="/usrx/local/dev/python/2.7.13/bin"
export platform=""

export myModules=${platform}"/gpfs/hps3/nos/noscrub/nwprod/csdlpy-1.5.1"
export pythonCode=${platform}"/gpfs/hps3/nos/noscrub/nwprod/hsofs-preView-1.5.1/preview/pre.py"
export logFile=${platform}"/gpfs/hps3/nos/noscrub/polar/preview/preview.log"

export aswipPath=${platform}"/gpfs/hps3/nos/noscrub/Yuji.Funakoshi/Dev-hsofs.v2.0.1/exec/hsofs_aswip"
export stormID="al802018"
export stormCycle="2018050712"
export aDeck=${platform}"/gpfs/gp1/nhc/save/guidance/storm-data/zsurge/al182018/al802018.fst"
export bDeck=${platform}"/gpfs/gp1/nhc/save/guidance/storm-data/zsurge/bal182018/bal802018.dat"

export outputDir=${platform}"/gpfs/hps3/nos/noscrub/polar/preview/"
export tmpDir=${platform}"/gpfs/hps3/nos/noscrub/tmp/preview/"
export pltCfgFile=${platform}"/gpfs/hps3/nos/noscrub/nwprod/hsofs-preView-1.5.1/scripts/config.plot.hsofs.ini"

export ftpLogin="svinogradov@emcrzdm"
export ftpPath="/home/www/polar/estofs/hsofs/preview/"

cd ${tmpDir}
PYTHONPATH=${myModules} ${pyPath}/python -W ignore ${pythonCode} -w ${aswipPath} -i ${stormID} -c ${stormCycle} -a ${aDeck} -b ${bDeck} -o ${outputDir} -t ${tmpDir} -p ${pltCfgFile} -u ${ftpLogin} -f ${ftpPath} # > ${logFile}
