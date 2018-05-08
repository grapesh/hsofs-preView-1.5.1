#!/bin/bash

## Load Python 2.7.13
#module use /usrx/local/dev/modulefiles
#module load python/2.7.13

export pyPath="/usrx/local/dev/python/2.7.13/bin"
export platform=""

export myModules=${platform}"/gpfs/hps3/nos/noscrub/nwprod/csdlpy-1.5.1"
export pythonCode=${platform}"/gpfs/hps3/nos/noscrub/nwprod/hsofs-preView-1.5.1/preview/pre.py"
export logFile=${platform}"/gpfs/hps3/nos/noscrub/polar/preview/preview.log"

export trackPath=${platform}"/gpfs/hps3/nos/noscrub/Yuji.Funakoshi/hsofs_preview/"
export stormID="al802018"
export stormCycle="2018050812"

export outputDir=${platform}"/gpfs/hps3/nos/noscrub/polar/preview/"
export tmpDir=${platform}"/gpfs/hps3/nos/noscrub/tmp/preview/"
export pltCfgFile=${platform}"/gpfs/hps3/nos/noscrub/nwprod/hsofs-preView-1.5.1/scripts/config.plot.hsofs.ini"

export ftpLogin="svinogradov@emcrzdm"
export ftpPath="/home/www/polar/estofs/hsofs/preview/"

cd ${tmpDir}
PYTHONPATH=${myModules} ${pyPath}/python -W ignore ${pythonCode} -w ${trackPath} -i ${stormID} -c ${stormCycle} -o ${outputDir} -t ${tmpDir} -p ${pltCfgFile} -u ${ftpLogin} -f ${ftpPath} # > ${logFile}
