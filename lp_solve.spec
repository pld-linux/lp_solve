Summary:	Library and tool that solves linear programming problem
Summary(pl):	Biblioteka i narzêdzie do rozwi±zywania problemu programowania liniowego
Name:		lp_solve
Version:	4.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.ics.ele.tue.nl/pub/lp_solve/%{name}_%{version}.tar.gz
Patch0:		%{name}-shared.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library and tool that solves linear programming problem using Simplex
algorithm.

%description -l pl
Biblioteka i narzêdzie do rozwi±zywania problemu programowania
liniowego przy u¿yciu algorytmu Simplex.

%package devel
Summary:	liblpk header files
Summary(pl):	Pliki nag³ówkowe biblioteki liblpk
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
liblpk header files.

%description devel -l pl
Pliki nag³ówkowe biblioteki liblpk.

%package static
Summary:	Static liblpk library
Summary(pl):	Statyczna biblioteka liblpk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static liblpk library.

%description static -l pl
Statyczna biblioteka liblpk.

%prep
%setup -q -n %{name}_%{version}
%patch -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
