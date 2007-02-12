%define		fversion	%(echo %{version} |tr r -)
%define		modulename	rgl
Summary:	3D visualization device system (OpenGL)
Summary(pl.UTF-8):   Sterownik wyświetlania 3D (OpenGL)
Name:		R-cran-%{modulename}
Version:	0.64r13
Release:	2
License:	GPL
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	bbbae92de0e3127cec4e8fd9d794d096
URL:		http://wsopuppenkiste.wiso.uni-goettingen.de/~dadler/rgl
BuildRequires:	R-base >= 2.4.0
BuildRequires:	XFree86-OpenGL-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
Requires(post,postun):	R-base >= 2.4.0
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
3D visualization device (OpenGL).

%description -l pl.UTF-8
Sterownik wyświetlania 3D (OpenGL).

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,README,README-X11}
%{_libdir}/R/library/%{modulename}
