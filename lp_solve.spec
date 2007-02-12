Summary:	Library and tool that solves linear programming problem
Summary(pl.UTF-8):   Biblioteka i narzędzie do rozwiązywania problemu programowania liniowego
Name:		lp_solve
Version:	4.0
Release:	2
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.ics.ele.tue.nl/pub/lp_solve/%{name}_%{version}.tar.gz
# Source0-md5:	58892f708d7f78664bce80c1ebc250f9
Patch0:		%{name}-shared.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library and tool that solves linear programming problem using Simplex
algorithm.

%description -l pl.UTF-8
Biblioteka i narzędzie do rozwiązywania problemu programowania
liniowego przy użyciu algorytmu Simplex.

%package devel
Summary:	liblpk header files
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki liblpk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
liblpk header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki liblpk.

%package static
Summary:	Static liblpk library
Summary(pl.UTF-8):   Statyczna biblioteka liblpk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liblpk library.

%description static -l pl.UTF-8
Statyczna biblioteka liblpk.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

rm -f lp_examples/*.{out,mps}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG MIPLIB_RESULTS MPS.description NETLIB_RESULTS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc HARTMUT_DOCUMENTATION SOSInterpolation.pdf lp_examples
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
