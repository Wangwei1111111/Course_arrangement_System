��    a      $              ,  #   -  [   Q  q  �  :     "   Z     }  m   �  g   �  J   e	  ,   �	  I   �	  :   '
     b
     �
     �
  3   �
      �
  I   
  X   T  �   �  3   l  Y   �  !   �  i     v   �  <   �  1   :  ^   l     �  (   �               3     N  ?   h  g   �  !     &   2  B   Y  %   �  9   �  ?   �  *   <  5   g     �  )   �     �  �  �  \   �  @   �  H   1  P   z  D   �  &     2   7  �   j  '   �  ,     =   J  B   �  5   �  @     O   B     �  '   �  /   �  +   
  W   6  ;   �  -   �      �           9  "   Z  M   }  3   �  ,   �  !   ,    N     [  Y   d  $   �     �  �   �  6   �  �     +   �  !   �  ,   	  6   6     m     y     {     �  8   �     �  �  �  #   �   �   	!  3  �!  O   �#  V   !$     x$  �   �$  �   Q%  �   &  X   �&  �    '  �   �'  G   B(  A   �(  2   �(  Y   �(  :   Y)  �   �)  �   *  ~  �*  W   },  �   �,  D   s-  �   �-  �   �.  �   x/  v   0  �   y0     H1  c   `1     �1  :   �1  *   2  ,   J2  f   w2  �   �2  +   �3  U   �3  p   Q4  D   �4  �   5  {   �5  Z   6  ~   x6  -   �6  G   %7     m7  �  �7  �   w:  w   ;  �   �;  �   1<  g   �<  :   =  h   W=  �   �=  )   l>  9   �>  L   �>  Q   ?  F   o?  S   �?  W   
@  X   b@  U   �@  O   A  A   aA  �   �A  q   5B  F   �B  @   �B  X   /C  \   �C  J   �C  �   0D  X   �D  M   6E  O   �E  �  �E     �G  �   �G  J   �H  &   �H  �   I  w   �J  [  FK  F   �L  5   �L  A   M  j   aM     �M     �M  2   �M  &   N  O   :N     �N   	$ python -m notebook.auth password 
        DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.
         
        Set the tornado compression options for websocket connections.

        This value will be returned from :meth:`WebSocketHandler.get_compression_options`.
        None (default) will disable compression.
        A dict (even an empty one) will enable compression.

        See the tornado docs for WebSocketHandler.get_compression_options for details.
         
    webapp_settings is deprecated, use tornado_settings.
 %d active kernel %d active kernels %s does not exist (bytes/sec)
        Maximum rate at which stream output can be sent on iopub before they are
        limited. (msgs/sec)
        Maximum rate at which messages can be sent on iopub before they are
        limited. (sec) Time window used to 
        check the message and data rate limits. Allow the notebook to be run from root user. Alternatively use `%s` when working on the notebook's Javascript and LESS Cannot bind to localhost, using 127.0.0.1 as default ip
%s Could not set permissions on %s Currently running servers: DEPRECATED use base_url DEPRECATED use the nbserver_extensions dict instead DEPRECATED, use tornado_settings DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib. Deprecated: Use minified JS file or not, mainly use during dev to avoid JS recompilation Dict of Python modules to load as notebook server extensions.Entry values can be used to enable and disable the loading ofthe extensions. The extensions will be loaded in alphabetical order. Don't open the notebook in a browser after startup. ERROR: the notebook server could not be started because no available port could be found. Error loading server extension %s Extra keyword arguments to pass to `set_secure_cookie`. See tornado's set_secure_cookie docs for details. Extra paths to search for serving jinja templates.

        Can be used to override templates from notebook.templates. Extra variables to supply to jinja templates when rendering. Hint: run the following command to set a password If True, each line of output will be a JSON object with the details from the server info file. Interrupted... List currently running notebook servers. No answer for 5s: No such file or directory: %s No such notebook dir: '%r' No web browser found: %s. Notebook servers are configured to only be run with a password. One-time token used for opening a browser.
        Once used, this token cannot be used again.
         Path to search for custom.js, css Permission to listen on port %i denied Please use `%pylab{0}` or `%matplotlib{0}` in the notebook itself. Produce machine-readable JSON output. Reraise exceptions encountered loading server extensions? Running as root is not recommended. Use --allow-root to bypass. Serving notebooks from local directory: %s Set the Access-Control-Allow-Credentials: true header Shutdown confirmed Shutdown this notebook server (%s/[%s])?  Shutting down %d kernels Specify Where to open the notebook on startup. This is the
        `new` argument passed to the standard library method `webbrowser.open`.
        The behaviour is not guaranteed, but depends on browser support. Valid
        values are:
            2 opens a new tab,
            1 opens a new window,
            0 opens in an existing window.
        See the `webbrowser.open` documentation for details.
         Supply SSL options for the tornado HTTPServer.
            See the tornado docs for details. Supply extra arguments that will be passed to Jinja environment. Supply overrides for terminado. Currently only supports "shell_command". Supply overrides for the tornado.web.Application that the Jupyter notebook uses. Support for specifying --pylab on the command line has been removed. Terminals not available (error was %s) The IP address the notebook server will listen on. The Jupyter HTML Notebook.
    
    This launches a Tornado based HTML Notebook Server that serves up an HTML5/Javascript Notebook client. The Jupyter Notebook is running at:
%s The Jupyter Notebook requires tornado >= 4.0 The Jupyter Notebook requires tornado >= 4.0, but you have %s The Jupyter Notebook requires tornado >= 4.0, but you have < 1.1.0 The MathJax.js configuration file that is to be used. The `ignore_minified_js` flag is deprecated and no longer works. The `ignore_minified_js` flag is deprecated and will be removed in Notebook 6.0 The config manager class to use The default URL to redirect to from `/` The directory to use for notebooks and kernels. The file where the cookie secret is stored. The full path to a certificate authority certificate for SSL/TLS client authentication. The full path to a private key file for usage with SSL/TLS. The full path to an SSL/TLS certificate file. The kernel manager class to use. The login handler class to use. The logout handler class to use. The notebook manager class to use. The number of additional ports to try if the specified port is not available. The port %i is already in use, trying another port. The port the notebook server will listen on. The session manager class to use. Token used for authenticating first-time connections to the server.

        When no password is enabled,
        the default is to generate a new, random token.

        Setting to an empty string disables authentication altogether, which is NOT RECOMMENDED.
         Untitled Use Control-C to stop this server and shut down all kernels (twice to skip confirmation). Using MathJax configuration file: %s Using MathJax: %s Welcome to Project Jupyter! Explore the various tools available and their corresponding documentation. If you are interested in contributing to the platform, please visit the communityresources section at http://jupyter.org/community.html. Whether to allow the user to run the notebook as root. Whether to trust or not X-Scheme/X-Forwarded-Proto and X-Real-Ip/X-Forwarded-For headerssent by the upstream reverse proxy. Necessary if the proxy handles SSL Writing notebook server cookie secret to %s [all ip addresses on your system] base_project_url is deprecated, use base_url extra paths to look for Javascript notebook extensions interrupted n received signal %s, stopping resuming operation... server_extensions is deprecated, use nbserver_extensions y Project-Id-Version: Jupyter VERSION
Report-Msgid-Bugs-To: EMAIL@ADDRESS
POT-Creation-Date: 2017-07-08 21:52-0500
PO-Revision-Date: 2020-07-06 17:38+0500
Last-Translator: Dmitriy Q <dmitry@atsip.ru>
Language: ru_RU
Language-Team: TranslAster <https://github.com/translaster>
Plural-Forms: nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<12 || n%100>14) ? 1 : 2);
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.10.3
 	$ python -m notebook.auth password 
        Отключено: используйте %pylab или %matplotlib в блокноте чтобы включить matplotlib.
          
        Установите параметры сжатия tornado для соединений websocket.

        Это значение будет возвращено из :meth: 'WebSocketHandler.get_compression_options`.
        None (по умолчанию) отключит сжатие.
        Диктат (даже пустой) будет включать сжатие.

        Смотрите документы tornado для WebSocketHandler.get_compression_options для получения подробной информации.
         
    web app_settings устарел, используйте tornado_settings.
 %d активное ядро %d активных ядра %d активных ядер %s не существует (байт/сек)
        Максимальная скорость отправки потока вывода на iopub, прежде
         чем он будет ограничен. (сообщ/сек)
        Максимальная скорость отправки сообщений на iopub, прежде
         чем они будут ограничены. (сек) Окно времени, используемое для 
          проверки ограничений скорости передачи сообщений и данных. Разрешить запускать блокнот от пользователя root. В качестве альтернативы используйте `%s` при работе с блокнотами Javascript и LESS Невозможно привязаться к localhost, используйте 127.0.0.1 в качестве ip-адреса по умолчанию
%s Не удалось установить разрешения для %s В настоящее время работают сервера: УСТАРЕЛО - используйте base_url УСТАРЕЛО - используйте nbserver_extensions вместо диктата УСТАРЕЛО - используйте tornado_settings ОТКЛЮЧЕНО: используйте %pylab или %matplotlib в блокноте чтобы включить matplotlib. Устарело: используйте уменьшенный файл JS или нет, в основном используется во время разработки чтобы избежать перекомпиляции JS Dict модулей Python для загрузки в качестве серверных расширений блокнотов. Введенные значения можно использовать для включения и отключения загрузки расширений. Расширения будут загружены в алфавитном порядке. Не открывайте блокнот в браузере после запуска. ОШИБКА: не удалось запустить сервер блокнота, так как не удалось найти доступный порт. Ошибка загрузки расширения сервера %s Дополнительные аргументы ключевого слова для передачи в `set_secure_cookie`. Подробнее см. документацию set_secure_cookie для tornado. Дополнительные пути для поиска обслуживающих шаблонов jinja.

        Может использоваться для переопределения шаблонов из notebook.templates. Дополнительные переменные для предоставления шаблонам jinja при рендеринге. Подсказка: выполните следующую команду, чтобы установить пароль Если True, то каждая строка вывода будет представлять собой объект JSON с подробностями из файла информации сервера. Прерывание... Список запущенных в данный момент серверов блокнотов. Нет ответа уже 5с: Нет такого файла или каталога: %s Нет такого блокнота: '%r' Веб-браузер не найден: %s. Серверы блокнотов настроены на работу только с паролем. Одноразовый токен, используемый для открытия в браузере. 
        После использования этот токен не может быть использован снова.
         Путь для поиска custom.js, css Разрешение на прослушивание порта %i отклонено Пожалуйста, используйте `%pylab{0}` или `%matplotlib{0}` в самом блокноте. Произведите машиночитаемый вывод JSON. Повторно поднимаемые исключения, встречающиеся при загрузке серверных расширений? Запуск от имени root не рекомендуется. Используйте --allow-root для обхода. Обслуживание блокнотов из локального каталога: %s Установка контроль-доступа-разрешенные-учетные_данные: заголовок true Выключение подтверждено Выключить этот сервер блокнотов (%s/[%s])?  Выключить %d ядер Укажите где открывать блокнот при запуске. Это "новый"
        аргумент, передаваемый для стандартного метода библиотек `webbrowser.open`.
        Поведение не гарантируется, но зависит от поддержки браузера. Допустимыми
        значениями являются:
            2 открывает новую вкладку,
            1 открывает новое окно,
            0 открывается в существующем окне.
        См. документацию `webbrowser.open` для получения подробной информации.
         Предоставьте параметры SSL для HTTPServer tornado.
            Подробности смотрите в документации tornado. Предоставьте дополнительные аргументы, передаваемые в среду Jinja. Переопределение поставок для terminado. В настоящее время поддерживается только "shell_command". Перекрывает поставки для tornado.web. Приложение, использующее блокнот Jupyter. Поддержка указания --pylab в командной строке была удалена. Терминалы недоступны (ошибка: %s) IP-адрес, который будет прослушиваться сервером блокнота. The Jupyter HTML Notebook.
    
    Запускает сервер HTML Notebook на базе Tornado, обслуживающий клиент HTML5/Javascript Notebook. Jupyter Notebook запущен на:
%s Для Jupyter Notebook требуется tornado >= 4.0 Для Jupyter Notebook требуется tornado >= 4.0, но у вас %s Для Jupyter Notebook требуется tornado >= 4.0, но у вас < 1.1.0 Использовать файл конфигурации MathJax.js. Флаг `ignore_minified_js` устарел и больше не работает. Флаг `ignore_minified_js` устарел и будет удален в Notebook 6.0 Класс менеджера конфигурации для использования URL-адрес по умолчанию для перенаправления на `/` Каталог, используемый для блокнотов и ядер. Файл, в котором хранится пароль cookie. Полный путь к сертификату центра сертификации для SSL/TLS аутентификации клиента. Полный путь к файлу приватного ключа для использования с SSL/TLS. Полный путь к файлу сертификата с SSL/TLS. Используемый класс менеджера ядра. Используемый класс обработчика входа в систему. Используемый класс обработчика выхода из системы. Используемый класс менеджера блокнотов. Количество дополнительных портов, которые нужно попробовать, если указанный порт недоступен. Порт %i уже используется, попробуйте другой порт. Порт сервера блокнотов для прослушивания. Класс менеджера сеансов для использования. Токен, используемый для проверки подлинности при первом подключении к серверу.

        Когда пароль не включен,
        по умолчанию генерируется новый случайный токен.

        Установка пустой строки полностью отключает аутентификацию, что НЕ РЕКОМЕНДУЕТСЯ.
         Без названия Используйте Control-C, для остановки этого сервера и выключения всех ядер (дважды, чтобы пропустить подтверждение). Использование файла конфигурации MathJax: %s Использование MathJax: %s Добро пожаловать в проект Jupyter! Изучите различные доступные инструменты и соответствующую им документацию. Если вы заинтересованы в том, чтобы внести свой вклад в платформу, пожалуйста, посетите раздел ресурсов сообщества по адресу http://jupyter.org/community.html. Следует ли разрешить пользователю запускать блокнот от имени root. Стоит ли доверять или нет Х-схеме/х-перенаправлению-прото и X-реал-ip/х-перенаправлению-для заголовков, загружаемых по потоку обратного прокси-сервера. Необходимо, если прокси обрабатывает SSL Запись пароля cookie сервера блокнота в %s [все ip-адреса в вашей системе] base_project_url устарел - используйте base_url дополнительные пути для поиска расширений блокнота Javascript прервано н получен сигнал %s, остановка возобновить работу... server_extensions устарело - используйте nbserver_extensions д 