Python Application Development - Core Classes 

 Modules:

   * Configuration File Support

   * Database Support

   * Logging Support

   * Emailing Support

   * Object-like syntax for Dictionaries (odict)

 Details:

   * Configuration Module
    
       Usage:
       
          # To create a singleton instance of configuration data
          # found in a yaml file pointed to by an environment
          # variable called VCONF
          
          from vlib import conf
          myconf = conf.Factory.create().data

          # Print configuration data, from a Yaml file that looks
          # like this:
          #
          # database:
          #    engine: mysql
          #    host: localhost
          #    db: vlibtests
          #    user: vlibtests
          #    passwd: bogangles

          print myconf['database']['hostname']
