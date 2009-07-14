%define upstream_name    txt2html
%define module_name      HTML-TextToHTML
%define upstream_version 2.51

Name:       perl-%{module_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Convert plain text file to HTML
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Provides:   %{upstream_name}
BuildArch:  noarch
# dependencies of txt2html script, not gathered automatically because of #52267
Requires:   perl(Pod::Usage)
Requires:   perl(Getopt::Long)
Requires:   perl(File::Basename)
Requires:   perl(Getopt::ArgvFile)

%description
HTML::TextToHTML converts plain text files to HTML. The txt2html
script uses this module to do the same from the command-line.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes TODO
%{_bindir}/txt2html
%{_mandir}/man1/txt2html.1*
%{_mandir}/man3/HTML*
%perl_vendorlib/HTML*

