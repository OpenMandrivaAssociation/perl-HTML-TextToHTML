%define upstream_name    txt2html
%define module_name      HTML-TextToHTML
%define upstream_version 2.5201

Name:		perl-%{module_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Convert plain text file to HTML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/txt2html-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Module::Build)

BuildArch:	noarch
# dependencies of txt2html script, not gathered automatically because of #52267
Requires:	perl(Pod::Usage)
Requires:	perl(Getopt::Long)
Requires:	perl(File::Basename)
Requires:	perl(Getopt::ArgvFile)
Provides:	%{upstream_name} = %{version}-%{release}

%description
HTML::TextToHTML converts plain text files to HTML. The txt2html
script uses this module to do the same from the command-line.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot}

%files
%doc README Changes TODO
%{_bindir}/txt2html
%{_mandir}/man1/txt2html.1*
%{_mandir}/man3/HTML*
%{perl_vendorlib}/HTML*

%changelog
* Tue Jul 14 2009 Anssi Hannula <anssi@mandriva.org> 2.510.0-1mdv2010.0
+ Revision: 395994
- initial Mandriva release


