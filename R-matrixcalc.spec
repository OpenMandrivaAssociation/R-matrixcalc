%global packname  matrixcalc
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.0.3
Release:          1
Summary:          Collection of functions for matrix differential calculus
Group:            Sciences/Mathematics
License:          GPL (>=2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/matrixcalc_1.0-3.tar.gz
BuildArch:        noarch
Requires:         R-core
BuildRequires:    R-devel
BuildRequires:    Rmath-devel
BuildRequires:    texlive-collection-latex 
BuildRequires:    pkgconfig(lapack)

%description
A collection of functions to support matrix differential calculus as
presented in Magnus and Neudecker (1999) Matrix Differential Calculus with
Applications in Statistics and Econometrics, Second Edition, John Wiley,
New York.  Some of the functions are comparable to APL and J functions
which are useful for actuarial models and calculations. This package is
used for teaching and research purposes at the Department of Finance and
Risk Engineering, Polytechnic University, Brooklyn, NY 11201.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0_1-1
+ Revision: 776239
- Import R-matrixcalc
- Import R-matrixcalc


