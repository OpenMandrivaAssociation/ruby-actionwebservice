%define rname actionwebservice
%define name ruby-%{rname}
%define version 1.2.6
%define release 6

Summary:	Web service support for Action Pack
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.rubyonrails.com/
Source0:	%{rname}-%{version}.gem
License:	MIT
Group:		Development/Ruby
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
Requires:	ruby ruby-actionpack ruby-activerecord

BuildRequires:	ruby-RubyGems 

%description
Adds WSDL/SOAP and XML-RPC web service support to Action Pack.

%prep
rm -rf %rname-%version
rm -rf tmp-%rname-%version
mkdir tmp-%rname-%version
gem install --ignore-dependencies %{SOURCE0} --no-rdoc --install-dir `pwd`/tmp-%rname-%version
mv tmp-%rname-%version/gems/%rname-%version .
mv tmp-%rname-%version/specifications/%rname-%version.gemspec %rname-%version/
rm -rf tmp-%rname-%version
%setup -T -D -n %rname-%version

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf %buildroot
mkdir -p $RPM_BUILD_ROOT{%{ruby_sitelibdir},%{ruby_ridir},%{ruby_gemdir}/specifications}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_sitelibdir}
cp -a ri/ActionWebService $RPM_BUILD_ROOT%{ruby_ridir}
cp -a %rname-%version.gemspec $RPM_BUILD_ROOT%{ruby_gemdir}/specifications/

for f in `find %buildroot%{ruby_sitelibdir} -name \*.rb`
do
        if head -n1 "$f" | grep '^#!' >/dev/null;
        then
                sed -i 's|/usr/local/bin|/usr/bin|' "$f"
                chmod 0755 "$f"
        else
                chmod 0644 "$f"
        fi
done


%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{ruby_sitelibdir}/*
%{ruby_ridir}/*
%{ruby_gemdir}/specifications/%rname-%version.gemspec
%doc CHANGELOG rdoc




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.2.6-5mdv2010.0
+ Revision: 433493
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2.6-4mdv2009.0
+ Revision: 260401
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2.6-3mdv2009.0
+ Revision: 251572
- rebuild

* Mon Jan 14 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1.2.6-1mdv2008.1
+ Revision: 151296
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 23 2007 Olivier Blin <oblin@mandriva.com> 1.2.3-1mdv2008.0
+ Revision: 17586
- 1.2.3

* Sat Apr 21 2007 Pascal Terjan <pterjan@mandriva.org> 1.1.6-2mdv2008.0
+ Revision: 16672
- ri is now in ri/ and not ri/ri/
- Use Development/Ruby group


* Thu Nov 16 2006 Olivier Blin <oblin@mandriva.com> 1.1.6-1mdv2007.0
+ Revision: 84944
- 1.1.6
- Import ruby-actionwebservice

* Sat Jul 29 2006 Olivier Blin <blino@mandriva.com> 1.1.4-1mdv2007.0
- 1.1.4
- don't version requires

* Mon Feb 13 2006 Pascal Terjan <pterjan@mandriva.org> 1.0.0-2mdk
- Fix Summary/URL/Description/Dependencies

* Mon Feb 13 2006 Pascal Terjan <pterjan@mandriva.org> 1.0.0-1mdk
- First Mandriva release

