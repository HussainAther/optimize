
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/athersh/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00outputq\x03csnakemake.io\nOutputFiles\nq\x04)\x81q\x05(X?\x00\x00\x00peak_out/macs2/sjl_s3_cp190_R1/sjl_s3_cp190_R1_peaks.narrowPeakq\x06X2\x00\x00\x00peak_out/macs2/sjl_s3_cp190_R1/sjl_s3_cp190_R1.bedq\x07e}q\x08(X\n\x00\x00\x00narrowPeakq\th\x06X\x03\x00\x00\x00bedq\nh\x07X\x06\x00\x00\x00_namesq\x0b}q\x0c(h\tK\x00N\x86q\rh\nK\x01N\x86q\x0euubX\x07\x00\x00\x00threadsq\x0fK\x01X\x04\x00\x00\x00ruleq\x10X\x05\x00\x00\x00macs2q\x11X\x06\x00\x00\x00paramsq\x12csnakemake.io\nParams\nq\x13)\x81q\x14(X\x1e\x00\x00\x00peak_out/macs2/sjl_s3_cp190_R1q\x15X\x0f\x00\x00\x00sjl_s3_cp190_R1q\x16e}q\x17(X\x06\x00\x00\x00prefixq\x18h\x15X\x0e\x00\x00\x00wrapper_sampleq\x19h\x16h\x0b}q\x1a(h\x18K\x00N\x86q\x1bh\x19K\x01N\x86q\x1cuubX\x06\x00\x00\x00configq\x1d}q\x1eX\t\x00\x00\x00resourcesq\x1fcsnakemake.io\nResources\nq )\x81q!(K\x01K\x01e}q"(X\x06\x00\x00\x00_coresq#K\x01X\x06\x00\x00\x00_nodesq$K\x01h\x0b}q%(h#K\x00N\x86q&h$K\x01N\x86q\'uubX\x03\x00\x00\x00logq(csnakemake.io\nLog\nq))\x81q*}q+h\x0b}q,sbX\x05\x00\x00\x00inputq-csnakemake.io\nInputFiles\nq.)\x81q/(X\x19\x00\x00\x00dedup/sjl_s3_input_R1.bamq0X\x19\x00\x00\x00dedup/sjl_s3_cp190_R1.bamq1e}q2(X\x03\x00\x00\x00inpq3h0X\x02\x00\x00\x00ipq4h1h\x0b}q5(h3K\x00N\x86q6h4K\x01N\x86q7uubX\t\x00\x00\x00wildcardsq8csnakemake.io\nWildcards\nq9)\x81q:h\x16a}q;(X\x06\x00\x00\x00sampleq<h\x16h\x0b}q=X\x06\x00\x00\x00sampleq>K\x00N\x86q?subub.')
######## Original script #########
from snakemake.shell import shell

shell(
    'macs2 '
    'callpeak '
    '-c {snakemake.input.inp} '
    '-t {snakemake.input.ip} '
    '--bdg --SPMR '
    '-n {snakemake.wildcards.sample} '
    '--outdir {snakemake.params.prefix}'
)
shell('Rscript {snakemake.params.prefix}/{snakemake.params.wrapper_sample}_model.r')
shell("ln -sf {snakemake.output.narrowPeak} {snakemake.output.bed}")
