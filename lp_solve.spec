# TODO
# - update -pl
%define		_ver_major	5.5
%define		_ver_minor	0.10
Summary:	Mixed Integer Linear Program solver
Summary(pl.UTF-8):	Biblioteka i narzędzie do rozwiązywania problemu programowania liniowego
Name:		lp_solve
Version:	%{_ver_major}.%{_ver_minor}
Release:	0.3
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/lpsolve/%{name}_%{version}_source.tar.gz
# Source0-md5:	26b3e95ddf3d9c077c480ea45874b3b8
Patch0:		%{name}-shared.patch
URL:		http://sourceforge.net/projects/lpsolve/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The linear programming (LP) problem can be formulated as: Solve A.x >=
V1, with V2.x maximal. A is a matrix, x is a vector of (nonnegative)
variables, V1 is a vector called the right hand side, and V2 is a
vector specifying the objective function.

An integer linear programming (ILP) problem is an LP with the
constraint that all the variables are integers. In a mixed integer
linear programming (MILP) problem, some of the variables are integer
and others are real.

The program lp_solve solves LP, ILP, and MILP problems. It is slightly
more general than suggested above, in that every row of A (specifying
one constraint) can have its own (in)equality, <=, >= or =. The result
specifies values for all variables.

lp_solve uses the 'Simplex' algorithm and sparse matrix methods for
pure LP problems. If one or more of the variables is declared integer,
the Simplex algorithm is iterated with a branch and bound algorithm,
until the desired optimal solution is found. lp_solve can read MPS
format input files.

%description -l pl.UTF-8
Biblioteka i narzędzie do rozwiązywania problemu programowania
liniowego przy użyciu algorytmu Simplex.

%package devel
Summary:	liblpsolve header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki liblpsolve
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
liblpsolve header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki liblpsolve.

%package static
Summary:	Static liblpsolve library
Summary(pl.UTF-8):	Statyczna biblioteka liblpsolve
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liblpsolve library.

%description static -l pl.UTF-8
Statyczna biblioteka liblpsolve.

%prep
%setup -q -n %{name}_%{_ver_major}
%patch0 -p1

%build
cd lpsolve55
CC="%{__cc}" CFLAGS="%{rpmcflags}" sh -x ccc
cd ../lp_solve
CC="%{__cc}" CFLAGS="%{rpmcflags}" sh -x ccc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/lpsolve}

install lp_solve/lp_solve $RPM_BUILD_ROOT%{_bindir}/lpsolve
install lpsolve55/liblpsolve55.a $RPM_BUILD_ROOT%{_libdir}/liblpsolve.a
install lpsolve55/liblpsolve55.so $RPM_BUILD_ROOT%{_libdir}/liblpsolve.so
cp -a lp*.h $RPM_BUILD_ROOT%{_includedir}/lpsolve

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/lpsolve
%attr(755,root,root) %{_libdir}/liblpsolve.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/lpsolve

%files static
%defattr(644,root,root,755)
%{_libdir}/liblpsolve.a
