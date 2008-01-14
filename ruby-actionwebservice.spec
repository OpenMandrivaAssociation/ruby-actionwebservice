%define rname actionwebservice
%define name ruby-%{rname}
%define version 1.2.6
%define release %mkrel 1

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


