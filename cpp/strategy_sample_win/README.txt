windows编译 示例使用vs2019, 需要自行安装


cl /c /I. /I.\extras\swf_oes\include /W3 /WX- /diagnostics:column /MP /O2 /Ob2 /D WIN32 /D _WINDOWS /D _CRT_SECURE_NO_DEPRECATE /D NDEBUG /D _MBCS /Gm- /EHsc /MD /Zp8 /GS /Gy /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /std:c++17 /external:W3 /Gd /TP /errorReport:queue /utf-8 /Zc:__cplusplus /Oxt /Zc:__cplusplus .\strategy_sample.cpp

link.exe /ERRORREPORT:QUEUE /OUT:".\strategy_sample.exe" /INCREMENTAL:NO /NOLOGO .\libs\win64\Release\client_api.0.17.4.3.1.lib kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /MACHINE:X64  /machine:x64 .\strategy_sample.obj

