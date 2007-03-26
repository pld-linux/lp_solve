# TODO
# - update -pl
%define		_ver_major	5.5
%define		_ver_minor	0.10
Summary:	Mixed Integer Linear Program solver
Summary(pl.UTF-8):	Biblioteka i narzędzie do rozwiązywania problemu programowania liniowego
Name:		lp_solve
Version:	%{_ver_major}.%{_ver_minor}
Release:	0.1
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
Mixed Integer Linear Programming (MILP) solver lp_solve solves pure
linear, (mixed) integer/binary, semi-continuous and special ordered
sets (SOS) models.

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