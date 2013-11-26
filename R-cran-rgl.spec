%define		fversion	%(echo %{version} |tr r -)
%define		modulename	rgl
Summary:	3D visualization device system (OpenGL)
Summary(pl.UTF-8):	Sterownik wyświetlania 3D (OpenGL)
Name:		R-cran-%{modulename}
Version:	0.93.991
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	9738b4d0dc4433d76cc7a9f5d14049d3
URL:		http://rgl.neoscientists.org/
BuildRequires:	R >= 2.8.1
BuildRequires:	OpenGL-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
Requires(post,postun):	R >= 2.8.1
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
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,README}
%{_libdir}/R/library/%{modulename}
