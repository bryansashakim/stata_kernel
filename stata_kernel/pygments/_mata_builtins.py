mata_builtins = (
    'AsArray_char',
    'AsArray_dup',
    'AsArray_top',
    'Cdhms',
    'Chms',
    'Clock',
    'Cmdyhms',
    'Cofc',
    'Cofd',
    'Corr',
    'Corrslowly',
    'Dmatrix',
    'Fden',
    'Ftail',
    'Hilbert',
    'Kmatrix',
    'LA_DGBMV',
    'LA_DGEBAK',
    'LA_DGEBAL',
    'LA_DGEES',
    'LA_DGEEV',
    'LA_DGEHRD',
    'LA_DGGBAK',
    'LA_DGGBAL',
    'LA_DGGHRD',
    'LA_DHGEQZ',
    'LA_DHSEIN',
    'LA_DHSEQR',
    'LA_DLAMCH',
    'LA_DORGHR',
    'LA_DSYEVX',
    'LA_DTGEVC',
    'LA_DTGSEN',
    'LA_DTREVC',
    'LA_DTRSEN',
    'LA_ZGEBAK',
    'LA_ZGEBAL',
    'LA_ZGEES',
    'LA_ZGEEV',
    'LA_ZGEHRD',
    'LA_ZGGBAK',
    'LA_ZGGBAL',
    'LA_ZGGHRD',
    'LA_ZHGEQZ',
    'LA_ZHSEIN',
    'LA_ZHSEQR',
    'LA_ZTGEVC',
    'LA_ZTGSEN',
    'LA_ZTREVC',
    'LA_ZTRSEN',
    'LA_ZUNGHR',
    'Lmatrix',
    'Toeplitz',
    'Vandermonde',
    '_chdir',
    '_cholesky',
    '_cholinv',
    '_cholsolve',
    '_collate',
    '_conj',
    '_corr',
    '_deriv',
    '_deriv_result_Hessian',
    '_deriv_result_Jacobian',
    '_deriv_result_gradient',
    '_deriv_result_scores',
    '_deriv_result_values',
    '_diag',
    '_docx_add_data',
    '_docx_add_mata',
    '_docx_close',
    '_docx_closeall',
    '_docx_image_add',
    '_docx_new',
    '_docx_new_table',
    '_docx_paragraph_add_text',
    '_docx_paragraph_new',
    '_docx_paragraph_new_styledtext',
    '_docx_save',
    '_docx_table_mod_cell_image',
    '_editmissing',
    '_edittoint',
    '_edittointtol',
    '_edittozero',
    '_edittozerotol',
    '_editvalue',
    '_eigensystem',
    '_eigenvalues',
    '_equilc',
    '_equilr',
    '_equilrc',
    '_error',
    '_fclose',
    '_fft',
    '_fget',
    '_fgetmatrix',
    '_fgetnl',
    '_fillmissing',
    '_flopin',
    '_flopout',
    '_fopen',
    '_fput',
    '_fputmatrix',
    '_fread',
    '_fseek',
    '_ftell',
    '_ftruncate',
    '_fullsvd',
    '_fwrite',
    '_geigen_la',
    '_geigenselectf_la',
    '_geigensystem_la',
    '_ghessenbergd',
    '_ghessenbergd_la',
    '_ghk',
    '_gschurd',
    '_gschurd_la',
    '_gschurdgroupby',
    '_gschurdgroupby_la',
    '_halton',
    '_hessenbergd',
    '_hessenbergd_la',
    '_hqrd',
    '_hqrdp',
    '_hqrdp_la',
    '_hqrdq1',
    '_invfft',
    '_invsym',
    '_jumble',
    '_lefteigensystem',
    '_lowertriangle',
    '_lud',
    '_lud_la',
    '_luinv',
    '_luinv_la',
    '_lusolve',
    '_lusolve_la',
    '_makesymmetric',
    '_matexpsym',
    '_matlogsym',
    '_matpowersym',
    '_mkdir',
    '_moptimize',
    '_moptimize_evaluate',
    '_negate',
    '_optimize',
    '_optimize_evaluate',
    '_perhapsequilc',
    '_perhapsequilr',
    '_perhapsequilrc',
    '_pinv',
    '_qrinv',
    '_qrsolve',
    '_quadrunningsum',
    '_rmdir',
    '_runningsum',
    '_schurd',
    '_schurd_la',
    '_schurdgroupby',
    '_schurdgroupby_la',
    '_solvelower',
    '_solvenl_init_argument',
    '_solvenl_init_conv_iterchng',
    '_solvenl_init_conv_maxiter',
    '_solvenl_init_conv_nearzero',
    '_solvenl_init_damping',
    '_solvenl_init_evaluator',
    '_solvenl_init_iter_dot',
    '_solvenl_init_iter_dot_indent',
    '_solvenl_init_iter_log',
    '_solvenl_init_numeq',
    '_solvenl_init_startingvals',
    '_solvenl_init_technique',
    '_solvenl_init_type',
    '_solvenl_solve',
    '_solveupper',
    '_sort',
    '_st_addobs',
    '_st_addvar',
    '_st_data',
    '_st_global',
    '_st_macroexpand',
    '_st_sdata',
    '_st_sstore',
    '_st_store',
    '_st_tsrevar',
    '_st_varindex',
    '_stata',
    '_strtoreal',
    '_sublowertriangle',
    '_substr',
    '_svd',
    '_svd_la',
    '_svdsv',
    '_svsolve',
    '_symeigen_la',
    '_symeigenselect_la',
    '_symeigensystem',
    '_symeigenvalues',
    '_tokenget',
    '_transpose',
    '_transposeonly',
    '_unlink',
    '_uppertriangle',
    'abbrev',
    'abs',
    'acos',
    'acosh',
    'adosubdir',
    'all',
    'allof',
    'any',
    'anyof',
    'arg',
    'args',
    'asarray',
    'asarray_contains',
    'asarray_contents',
    'asarray_create',
    'asarray_elements',
    'asarray_first',
    'asarray_key',
    'asarray_keys',
    'asarray_next',
    'asarray_notfound',
    'asarray_remove',
    'ascii',
    'asin',
    'asinh',
    'assert',
    'asserteq',
    'atan',
    'atan2',
    'atanh',
    'betaden',
    'binomial',
    'binomialp',
    'binomialtail',
    'binormal',
    'blockdiag',
    'bofd',
    'breakkey',
    'breakkeyreset',
    'bufbfmtisnum',
    'bufbfmtlen',
    'bufbyteorder',
    'bufget',
    'bufio',
    'bufmissingvalue',
    'bufput',
    'byteorder',
    'callersversion',
    'cat',
    'ceil',
    'char',
    'chdir',
    'chi2',
    'chi2den',
    'chi2tail',
    'cholesky',
    'cholinv',
    'cholsolve',
    'clock',
    'cloglog',
    'cofC',
    'cofd',
    'collate',
    'colmax',
    'colmaxabs',
    'colmin',
    'colminmax',
    'colmissing',
    'colnonmissing',
    'cols',
    'colscalefactors',
    'colshape',
    'colsum',
    'comb',
    'cond',
    'conj',
    'convolve',
    'corr',
    'correlation',
    'cos',
    'cosh',
    'crexternal',
    'cross',
    'crossdev',
    'cvpermute',
    'cvpermutesetup',
    'date',
    'day',
    'deconvolve',
    'deriv',
    'deriv_init',
    'deriv_init_argument',
    'deriv_init_evaluator',
    'deriv_init_h',
    'deriv_init_params',
    'deriv_init_verbose',
    'deriv_init_weights',
    'deriv_query',
    'deriv_result_Hessian',
    'deriv_result_Jacobian',
    'deriv_result_errorcode',
    'deriv_result_gradient',
    'deriv_result_h',
    'deriv_result_returncode',
    'deriv_result_scores',
    'deriv_result_value',
    'deriv_result_values',
    'designmatrix',
    'det',
    'dettriangular',
    'dgammapda',
    'dgammapdada',
    'dgammapdadx',
    'dgammapdx',
    'dgammapdxdx',
    'dhms',
    'diag',
    'diag0cnt',
    'diagonal',
    'digamma',
    'dir',
    'direxists',
    'direxternal',
    'display',
    'displayas',
    'displayflush',
    'dofC',
    'dofb',
    'dofc',
    'dofh',
    'dofm',
    'dofq',
    'dofw',
    'dofy',
    'dow',
    'doy',
    'dsign',
    'dunnettprob',
    'editmissing',
    'edittoint',
    'edittointtol',
    'edittozero',
    'edittozerotol',
    'editvalue',
    'eigensystem',
    'eigensystemselectf',
    'eigensystemselecti',
    'eigensystemselectr',
    'eigenvalues',
    'eltype',
    'epsilon',
    'error',
    'errprintf',
    'exit',
    'exp',
    'factorial',
    'favorspeed',
    'fbufget',
    'fbufput',
    'fclose',
    'ferrortext',
    'fft',
    'fget',
    'fgetmatrix',
    'fgetnl',
    'fileexists',
    'findexternal',
    'findfile',
    'floatround',
    'floor',
    'fmtwidth',
    'fopen',
    'fput',
    'fputmatrix',
    'fread',
    'freturncode',
    'frombase',
    'fseek',
    'fstatus',
    'ftell',
    'ftfreqs',
    'ftpad',
    'ftperiodogram',
    'ftretime',
    'ftruncate',
    'ftunwrap',
    'ftwrap',
    'fullsdiag',
    'fullsvd',
    'fwrite',
    'gamma',
    'gammaden',
    'gammap',
    'gammaptail',
    'geigensystem',
    'geigensystemselectf',
    'geigensystemselectr',
    'ghalton',
    'ghessenbergd',
    'ghk',
    'ghk_init',
    'ghk_query_npts',
    'ghkfast',
    'ghkfast_i',
    'ghkfast_init',
    'gschurd',
    'gschurdgroupby',
    'halfyear',
    'halfyearly',
    'halton',
    'hash1',
    'hasmissing',
    'hessenbergd',
    'hhC',
    'hms',
    'hofd',
    'hours',
    'hqrd',
    'hqrdmultq',
    'hqrdmultq1t',
    'hqrdp',
    'hqrdq',
    'hqrdq1',
    'hqrdr',
    'hqrdr1',
    'hypergeometric',
    'hypergeometricp',
    'ibeta',
    'ibetatail',
    'inbase',
    'indexnot',
    'init',
    'invF',
    'invFtail',
    'invHilbert',
    'invbinomial',
    'invbinomialtail',
    'invchi2',
    'invchi2tail',
    'invcloglog',
    'invdunnettprob',
    'invfft',
    'invgammap',
    'invgammaptail',
    'invibeta',
    'invibetatail',
    'invlogit',
    'invnFtail',
    'invnbinomial',
    'invnbinomialtail',
    'invnchi2',
    'invnchi2tail',
    'invnibeta',
    'invnormal',
    'invnttail',
    'invorder',
    'invpoisson',
    'invpoissontail',
    'invsym',
    'invt',
    'invtokens',
    'invttail',
    'invtukeyprob',
    'invvech',
    'iscomplex',
    'isdiagonal',
    'isfleeting',
    'ispointer',
    'isreal',
    'isrealvalues',
    'isstring',
    'issymmetric',
    'issymmetriconly',
    'isview',
    'jumble',
    'lefteigensystem',
    'lefteigensystemselectf',
    'lefteigensystemselecti',
    'lefteigensystemselectr',
    'leftgeigensystem',
    'length',
    'liststruct',
    'lnfactorial',
    'lngamma',
    'lnnormal',
    'lnnormalden',
    'log',
    'log10',
    'logit',
    'lowertriangle',
    'lud',
    'luinv',
    'lusolve',
    'makesymmetric',
    'matexpsym',
    'matlogsym',
    'matpowersym',
    'max',
    'maxdouble',
    'maxindex',
    'mdy',
    'mdyhms',
    'mean',
    'meanvariance',
    'min',
    'mindouble',
    'minindex',
    'minmax',
    'minutes',
    'missing',
    'missingof',
    'mkdir',
    'mmC',
    'mod',
    'mofd',
    'month',
    'monthly',
    'moptimize',
    'moptimize_ado_cleanup',
    'moptimize_evaluate',
    'moptimize_init',
    'moptimize_init_by',
    'moptimize_init_evaluator',
    'moptimize_init_userinfo',
    'moptimize_query',
    'moptimize_result_V_robust',
    'moptimize_result_converged',
    'moptimize_result_display',
    'moptimize_util_by',
    'moptimize_util_eq_indices',
    'moptimize_util_matbysum',
    'moptimize_util_sum',
    'more',
    'mreldif',
    'mreldifre',
    'mreldifsym',
    'msofhours',
    'msofminutes',
    'msofseconds',
    'nFden',
    'nFtail',
    'nameexternal',
    'nbetaden',
    'nbinomial',
    'nbinomialp',
    'nbinomialtail',
    'nchi2',
    'nchi2den',
    'nchi2tail',
    'nibeta',
    'nonmissing',
    'norm',
    'normal',
    'normalden',
    'npnF',
    'npnchi2',
    'npnt',
    'ntden',
    'nttail',
    'optimize',
    'optimize_evaluate',
    'optimize_init',
    'optimize_init_argument',
    'optimize_init_cluster',
    'optimize_init_colstripe',
    'optimize_init_constraints',
    'optimize_init_conv_ignorenrtol',
    'optimize_init_conv_maxiter',
    'optimize_init_conv_ptol',
    'optimize_init_conv_warning',
    'optimize_init_evaluations',
    'optimize_init_evaluator',
    'optimize_init_iterid',
    'optimize_init_negH',
    'optimize_init_nmsimplexdeltas',
    'optimize_init_params',
    'optimize_init_singularHmethod',
    'optimize_init_technique',
    'optimize_init_trace_dots',
    'optimize_init_tracelevel',
    'optimize_init_valueid',
    'optimize_init_verbose',
    'optimize_init_which',
    'optimize_query',
    'optimize_result_Hessian',
    'optimize_result_V',
    'optimize_result_V_oim',
    'optimize_result_V_opg',
    'optimize_result_converged',
    'optimize_result_errorcode',
    'optimize_result_errortext',
    'optimize_result_evaluations',
    'optimize_result_gradient',
    'optimize_result_iterationlog',
    'optimize_result_iterations',
    'optimize_result_params',
    'optimize_result_returncode',
    'optimize_result_scores',
    'optimize_result_value',
    'order',
    'orgtype',
    'panelsetup',
    'panelstats',
    'panelsubmatrix',
    'panelsubview',
    'pathasciisuffix',
    'pathbasename',
    'pathisabs',
    'pathisurl',
    'pathjoin',
    'pathlist',
    'pathrmsuffix',
    'pathsearchlist',
    'pathsplit',
    'pathstatasuffix',
    'pathsubsysdir',
    'pathsuffix',
    'pinv',
    'poisson',
    'poissonp',
    'poissontail',
    'polyadd',
    'polyderiv',
    'polydiv',
    'polyeval',
    'polyinteg',
    'polymult',
    'polyroots',
    'polysolve',
    'polytrim',
    'printf',
    'pwd',
    'qofd',
    'qrd',
    'qrdp',
    'qrinv',
    'qrsolve',
    'quadcolsum',
    'quadcorrelation',
    'quadcross',
    'quadcrossdev',
    'quadmeanvariance',
    'quadrant',
    'quadrowsum',
    'quadrunningsum',
    'quadsum',
    'quadvariance',
    'quarter',
    'quarterly',
    'querybreakintr',
    'range',
    'rangen',
    'rank',
    'rbeta',
    'rbinomial',
    'rchi2',
    'rdiscrete',
    'reldif',
    'revorder',
    'rgamma',
    'rhypergeometric',
    'rmdir',
    'rmexternal',
    'rnbinomial',
    'rnormal',
    'round',
    'rowmax',
    'rowmaxabs',
    'rowmin',
    'rowminmax',
    'rowmissing',
    'rownonmissing',
    'rows',
    'rowscalefactors',
    'rowshape',
    'rowsum',
    'rpoisson',
    'rseed',
    'runiform',
    'runningsum',
    'schurd',
    'schurdgroupby',
    'seconds',
    'select',
    'selectindex',
    'setbreakintr',
    'setmore',
    'setmoreonexit',
    'sign',
    'sin',
    'sinh',
    'sizeof',
    'smallestdouble',
    'solve_tol',
    'solvelower',
    'solvenl_dump',
    'solvenl_init',
    'solvenl_init_argument',
    'solvenl_init_conv_iterchng',
    'solvenl_init_conv_maxiter',
    'solvenl_init_conv_nearzero',
    'solvenl_init_damping',
    'solvenl_init_evaluator',
    'solvenl_init_iter_dot',
    'solvenl_init_iter_dot_indent',
    'solvenl_init_iter_log',
    'solvenl_init_numeq',
    'solvenl_init_startingvals',
    'solvenl_init_technique',
    'solvenl_init_type',
    'solvenl_result_Jacobian',
    'solvenl_result_conv_iter',
    'solvenl_result_conv_iterchng',
    'solvenl_result_conv_nearzero',
    'solvenl_result_converged',
    'solvenl_result_error_code',
    'solvenl_result_values',
    'solvenl_solve',
    'solveupper',
    'sort',
    'soundex',
    'soundex_nara',
    'spline3',
    'spline3eval',
    'sprintf',
    'sqrt',
    'ssC',
    'st_addobs',
    'st_addvar',
    'st_data',
    'st_dir',
    'st_dropobsif',
    'st_dropobsin',
    'st_dropvar',
    'st_eclear',
    'st_global',
    'st_global_hcat',
    'st_isfmt',
    'st_islmname',
    'st_isname',
    'st_isnumfmt',
    'st_isnumvar',
    'st_isstrfmt',
    'st_isstrvar',
    'st_keepobsif',
    'st_keepobsin',
    'st_keepvar',
    'st_local',
    'st_macroexpand',
    'st_matrix',
    'st_matrix_hcat',
    'st_matrixcolstripe',
    'st_matrixrowstripe',
    'st_nobs',
    'st_numscalar',
    'st_numscalar_hcat',
    'st_nvar',
    'st_rclear',
    'st_replacematrix',
    'st_sclear',
    'st_sdata',
    'st_select',
    'st_sstore',
    'st_store',
    'st_strscalar',
    'st_subview',
    'st_sview',
    'st_tempfilename',
    'st_tempname',
    'st_tsrevar',
    'st_updata',
    'st_varformat',
    'st_varindex',
    'st_varlabel',
    'st_varname',
    'st_varrename',
    'st_vartype',
    'st_varvaluelabel',
    'st_view',
    'st_viewobs',
    'st_viewvars',
    'st_vldrop',
    'st_vlexists',
    'st_vlload',
    'st_vlmap',
    'st_vlmodify',
    'st_vlsearch',
    'stata',
    'statasetversion',
    'stataversion',
    'stritrim',
    'strlen',
    'strlower',
    'strltrim',
    'strmatch',
    'strofreal',
    'strpos',
    'strproper',
    'strreverse',
    'strrtrim',
    'strtoname',
    'strtoreal',
    'strtrim',
    'strupper',
    'subinstr',
    'subinword',
    'sublowertriangle',
    'substr',
    'sum',
    'svd',
    'svdsv',
    'svsolve',
    'swap',
    'symeigensystem',
    'symeigensystemselectr',
    'symeigenvalues',
    'tan',
    'tanh',
    'tden',
    'tokenallowhex',
    'tokenallownum',
    'tokenget',
    'tokengetall',
    'tokeninit',
    'tokeninitstata',
    'tokenoffset',
    'tokenpchars',
    'tokenpeek',
    'tokenqchars',
    'tokenrest',
    'tokens',
    'tokenset',
    'tokenwchars',
    'trace',
    'transposeonly',
    'trigamma',
    'trunc',
    'ttail',
    'tukeyprob',
    'uniqrows',
    'unitcircle',
    'unlink',
    'unorder',
    'uppertriangle',
    'valofexternal',
    'variance',
    'vec',
    'vech',
    'week',
    'weekly',
    'whether_ssd',
    'wofd',
    'year',
    'yearly',
    'yofd'
)
