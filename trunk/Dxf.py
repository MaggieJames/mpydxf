#           GNU LESSER GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007
#
# Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.
#
#
#  This version of the GNU Lesser General Public License incorporates
#the terms and conditions of version 3 of the GNU General Public
#License, supplemented by the additional permissions listed below.
#
#  0. Additional Definitions. 
#
#  As used herein, "this License" refers to version 3 of the GNU Lesser
#General Public License, and the "GNU GPL" refers to version 3 of the GNU
#General Public License.
#
#  "The Library" refers to a covered work governed by this License,
#other than an Application or a Combined Work as defined below.
#
#  An "Application" is any work that makes use of an interface provided
#by the Library, but which is not otherwise based on the Library.
#Defining a subclass of a class defined by the Library is deemed a mode
#of using an interface provided by the Library.
#
#  A "Combined Work" is a work produced by combining or linking an
#Application with the Library.  The particular version of the Library
#with which the Combined Work was made is also called the "Linked
#Version".
#
#  The "Minimal Corresponding Source" for a Combined Work means the
#Corresponding Source for the Combined Work, excluding any source code
#for portions of the Combined Work that, considered in isolation, are
#based on the Application, and not on the Linked Version.
#
#  The "Corresponding Application Code" for a Combined Work means the
#object code and/or source code for the Application, including any data
#and utility programs needed for reproducing the Combined Work from the
#Application, but excluding the System Libraries of the Combined Work.
#
#  1. Exception to Section 3 of the GNU GPL.
#
#  You may convey a covered work under sections 3 and 4 of this License
#without being bound by section 3 of the GNU GPL.
#
#  2. Conveying Modified Versions.
#
#  If you modify a copy of the Library, and, in your modifications, a
#facility refers to a function or data to be supplied by an Application
#that uses the facility (other than as an argument passed when the
#facility is invoked), then you may convey a copy of the modified
#version:
#
#   a) under this License, provided that you make a good faith effort to
#   ensure that, in the event an Application does not supply the
#   function or data, the facility still operates, and performs
#   whatever part of its purpose remains meaningful, or
#
#   b) under the GNU GPL, with none of the additional permissions of
#   this License applicable to that copy.
#
#  3. Object Code Incorporating Material from Library Header Files.
#
#  The object code form of an Application may incorporate material from
#a header file that is part of the Library.  You may convey such object
#code under terms of your choice, provided that, if the incorporated
#material is not limited to numerical parameters, data structure
#layouts and accessors, or small macros, inline functions and templates
#(ten or fewer lines in length), you do both of the following:
#
#   a) Give prominent notice with each copy of the object code that the
#   Library is used in it and that the Library and its use are
#   covered by this License.
#
#   b) Accompany the object code with a copy of the GNU GPL and this license
#   document.
#
#  4. Combined Works.
#
#  You may convey a Combined Work under terms of your choice that,
#taken together, effectively do not restrict modification of the
#portions of the Library contained in the Combined Work and reverse
#engineering for debugging such modifications, if you also do each of
#the following:
#
#   a) Give prominent notice with each copy of the Combined Work that
#   the Library is used in it and that the Library and its use are
#   covered by this License.
#
#   b) Accompany the Combined Work with a copy of the GNU GPL and this license
#   document.
#
#   c) For a Combined Work that displays copyright notices during
#   execution, include the copyright notice for the Library among
#   these notices, as well as a reference directing the user to the
#   copies of the GNU GPL and this license document.
#
#   d) Do one of the following:
#
#       0) Convey the Minimal Corresponding Source under the terms of this
#       License, and the Corresponding Application Code in a form
#       suitable for, and under terms that permit, the user to
#       recombine or relink the Application with a modified version of
#       the Linked Version to produce a modified Combined Work, in the
#       manner specified by section 6 of the GNU GPL for conveying
#       Corresponding Source.
#
#       1) Use a suitable shared library mechanism for linking with the
#       Library.  A suitable mechanism is one that (a) uses at run time
#       a copy of the Library already present on the user's computer
#       system, and (b) will operate properly with a modified version
#       of the Library that is interface-compatible with the Linked
#       Version. 
#
#   e) Provide Installation Information, but only if you would otherwise
#   be required to provide such information under section 6 of the
#   GNU GPL, and only to the extent that such information is
#   necessary to install and execute a modified version of the
#   Combined Work produced by recombining or relinking the
#   Application with a modified version of the Linked Version. (If
#   you use option 4d0, the Installation Information must accompany
#   the Minimal Corresponding Source and Corresponding Application
#   Code. If you use option 4d1, you must provide the Installation
#   Information in the manner specified by section 6 of the GNU GPL
#   for conveying Corresponding Source.)
#
#  5. Combined Libraries.
#
#  You may place library facilities that are a work based on the
#Library side by side in a single library together with other library
#facilities that are not Applications and are not covered by this
#License, and convey such a combined library under terms of your
#choice, if you do both of the following:
#
#   a) Accompany the combined library with a copy of the same work based
#   on the Library, uncombined with any other library facilities,
#   conveyed under the terms of this License.
#
#   b) Give prominent notice with the combined library that part of it
#   is a work based on the Library, and explaining where to find the
#   accompanying uncombined form of the same work.
#
#  6. Revised Versions of the GNU Lesser General Public License.
#
#  The Free Software Foundation may publish revised and/or new versions
#of the GNU Lesser General Public License from time to time. Such new
#versions will be similar in spirit to the present version, but may
#differ in detail to address new problems or concerns.
#
#  Each version is given a distinguishing version number. If the
#Library as you received it specifies that a certain numbered version
#of the GNU Lesser General Public License "or any later version"
#applies to it, you have the option of following the terms and
#conditions either of that published version or of any later version
#published by the Free Software Foundation. If the Library as you
#received it does not specify a version number of the GNU Lesser
#General Public License, you may choose any version of the GNU Lesser
#General Public License ever published by the Free Software Foundation.
#
#  If the Library as you received it specifies that a proxy can decide
#whether future versions of the GNU Lesser General Public License shall
#apply, that proxy's public statement of acceptance of any version is
#permanent authorization for you to choose that version for the
#Library.

from DxfMaps import map_header
from string import *
from math import pi, cos, sin

class Header:
    
    def __init__(self, list_variables):
        """ It inserts Header 
        list_variable is a list of tuples: [(variable_name, value)...]"""
        map = map_header
        self.begin = [(2, "HEADER")]
        self.string = ""
        
        for each_variable in list_variables:
            self.string += "9\n"+"$"+str(each_variable[0])+"\n"+str(map[each_variable[0]][0])+"\n"+each_variable[1]+"\n"
    
    def write(self):
        return section(list_scan(self.begin)+self.string)
    
class Classes:
    
    def __init__(self, list_classes):
        """ It inserts Classes
        classes is list of tuples: [(class_dxf_record, class_name, app_name, flags)]
        flags is a list of tuples: [(code, value)...] """
        self.begin = [(2,"CLASSES")]
        self.string =""
        
        for each_class in list_classes:
            class_dxf_record, class_name, app_name, flags = each_class
            self.string += [ (0,"CLASS"),(1,class_dxf_record), (2,class_name), (3,app_name) ]
            for each_flag in flags:
                self.string += [ (each_flag[0], each_flag[1]) ]
    
    def write(self):
        return section(list_scan(self.begin)+self.string)
    
class Object:
    
    def __init__(self, begin_type_object, begin_handle, begin_list, entries, groups):
        self.begin = [(2,"OBJECTS")]
        self.begin2 = ""
        self.string = ""

        self.begin2 = [ (0, begin_type_object), (5, begin_handle) ]
        self.begin2 += list_scan(begin_list)
        self.string = list_scan(entries)
        self.string = list_scan(groups)
        
    def write(self):
        return section(list_scan(self.begin)+self.begin2+self.string)
    
class Tables:
    
    def __init__(self, entries):
        self.begin = [(2,"TABLES")]
        self.list_code = []
        
        for each_entry in entries:
            self.list_code += each_entry.begin+each_entry.begin2+each_entry.list_code
        
    def write(self):
        return section(list_scan(self.begin+self.list_code))

class Table:
    
    def __init__(self, type, records, max_entries):
        self.handle = handle_counter.get_handle()
        self.begin =     [(0,   "TABLE")]
        self.begin2 =    [(2,   type)]
        self.list_code = [(5,   self.handle),
                          (100, "AcDbSymbolTable"),
                          (70,   max_entries)]
        self.end =  [(0, "ENDTAB")]
        for each_record in records:
            self.list_code += each_record.begin+each_record.list_code
            #self.list_code.insert(4,(330, self.handle))
        self.list_code += self.end

class Blocks:
    
    def __init__(self, entries):
        #print "Entries",entries
        self.begin = [(2,"BLOCKS")]
        self.list_code = []
        
        for each_entry in entries:
            self.list_code += each_entry.list_code
            
    def write(self):
        return section(list_scan(self.begin+self.list_code))

class Block:
    
    def __init__(self, block_name, block_name_desc, entities, layer, bp=[0,0,0], block_flags=0):
        self.handle = handle_counter.get_handle()
        self.list_code =  [(0,"BLOCK"),
                           (8,  layer),
                           (2,  block_name),
                           (70, block_flags),
                           (10, bp[0]),
                           (20, bp[1]),
                           (30, bp[2]),
                           (3,  block_name_desc)]
        
        for each_entity in entities:
            self.list_code += each_entity.list_common_code+each_entity.list_code
        
        self.list_code += [(0, "ENDBLK"),
                           (5, self.handle),
                           (8, layer)]
           
    def write(self):
        return section(list_scan(self.begin)+self.list_code)

class TableLtypeRecord:
    
    def __init__(self, name, name_desc, pattern,  type_elements, pattern_length, flag_value=0):
        
        self.handle = handle_counter.get_handle()
        self.begin =     [(0,   "LTYPE")]
        self.list_code = [(2,   name),
                          (5,   self.handle),
                          (100, "AcDbSymbolTableRecord"),
                          (100, "AcDbLinetypeTableRecord"),
                          (3,   name_desc),
                          (70,  flag_value),
                          (72,  65),
                          (73,  type_elements),
                          (40,  pattern_length)]
        if pattern  is not None:
            
            for each_length in pattern:
                self.list_code.append((49,each_length[0]))
                #self.list_code.append((74,each_length[1]))
        print "ciao"
    def write(self):
        return list_scan(self.begin+self.begin2+self.list_code)
    
class TableLayerRecord:
    
    def __init__(self, layer_name,  color, linetype_name, standard_flags=0,):
        self.handle = handle_counter.get_handle()
        self.begin =     [(0,   "LAYER")]
        self.list_code = [(2,   layer_name),
                          (5,   self.handle),
                          (70,  standard_flags),
                          (62,  color),
                          (6,   linetype_name),
                          (100, "AcDbSymbolTableRecord"),
                          (100, "AcDbLayerTableRecord")                          
                          ]
        
class TableVPortRecord:
    
    def __init__(self, parent_handle, viewport_name, standard_flags, p_lower_left, p_upper_right, 
                 p_center, p_snap_base,
                 snap_spacing, grid_spacing, view_direction, p_view_target, lens_length,
                 front_clipping, back_clipping, view_height, snap_rotation_angle, view_twist_angle,
                  circle_sides, render_mode, ucs, ucs_x_axis, ucs_y_axis, ortho_type, elevation):

        self.begin = [(0, "VPORT")]
        self.handle = handle_counter.get_handle()
        self.list_code = [(5, self.handle),
                        #  (330, parent_handle),
                          (100, "AcDbSymbolTableRecord"),
                          (100, "AcDbViewportTableRecord"),
                          (2,   viewport_name),
                          (70,  standard_flags),
                          (10,  p_lower_left[0]),
                          (20,  p_lower_left[1]),
                          (10,  p_lower_left[0]),
                          (20,  p_lower_left[1]),
                          (11,  p_upper_right[0]),
                          (21,  p_upper_right[1]),
                          (12,  p_center[0]),
                          (22,  p_center[1]),
                          (13,  p_snap_base[0]),
                          (23,  p_snap_base[1]),
                          (14,  snap_spacing[0]),
                          (24,  snap_spacing[1]),
                          (15,  grid_spacing[0]),
                          (25,  grid_spacing[1]),
                          (16,  view_direction[0]),
                          (26,  view_direction[1]),
                          (36,  view_direction[2]),
                          (17,  p_view_target[0]),
                          (27,  p_view_target[1]),
                          (37,  p_view_target[2]),
                          (15,  grid_spacing[0]),
                          (25,  grid_spacing[1]),
                          (42,  lens_length),
                          (43,  front_clipping),
                          (44,  back_clipping),
                          (45,  view_height),
                          (50,  snap_rotation_angle),
                          (51,  view_twist_angle),
                          (72,  circle_sides),
                          (281, render_mode),
                          (110, ucs[0]),
                          (120, ucs[1]),
                          (130, ucs[2]),
                          (111, ucs_x_axis[0]),
                          (121, ucs_x_axis[1]),
                          (131, ucs_x_axis[2]),
                          (112, ucs_y_axis[0]),
                          (122, ucs_y_axis[1]),
                          (132, ucs_y_axis[2]),
                          (79,  ortho_type),
                          (146, elevation)]
        
class TableStyleRecord:
    
    """ It is the record to set Font style"""
    def __init__(self, style_name, last_height_used, primary_font_file_name,
                 fixed_text_height=0, big_font_file_name="",
                 oblique_angle=0, width_factor=1, standard_flags=0, text_generation=0):

        self.begin = [(0, "STYLE")]
        self.handle = handle_counter.get_handle()
        list = [(2,   style_name),
                (5,   self.handle),
                (70,  standard_flags),
                (100, "AcDbSymbolTableRecord"),
                (100, "AcDbStyleTableRecord"),
                (40,  fixed_text_height),
                (41,  width_factor ),
                (50,  oblique_angle),
                (71,  text_generation),
                (42,  last_height_used),
                (3,   primary_font_file_name ),
                (4,   big_font_file_name) ]
        self.list_code = filter_list(list)
        
class TableViewPortRecord:

    """ It is the record to set Font style"""
    def __init__(self):
        self.begin = [(0, "VPORT")]
        self.handle = handle_counter.get_handle()
        list = [(2, "*ACTIVE"),
                (70, 0),
                (10, 0),
                (20,0),
                (11, 1.0),
                (21, 1.0),
                (12, 5800),
                (22, 4200),
                (13, 0),
                (23, 0),
                (14, 1),
                (24, 1),
                (15, 0),
                (25, 0),
                (16, 0),
                (26, 0),
                (36, 1),
                (17, 0),
                (27, 0),
                (37, 0),
                (40, 10000),
                (41, 2),
                (42, 50),
                (43, 0),
                (44, 0),
                (50, 0),
                (51, 0),
                (71, 0),
                (72, 1000),
                (73, 1),
                (74, 0),
                (75, 0),
                (76, 0),
                (77, 0),
                (78, 1)]

        self.list_code = filter_list(list)

class TableDimStyleRecord:
    
    def __init__(self, style_name, blocks, attrib):
        self.begin = [(0, "DIMSTYLE")]
        list = [(2, style_name),    # Dimension style name
                (70, 0),
                (3, " "),
                (4, " "),
                (5, blocks[0]),   # Names of the blocks used for arrows 
                (6, blocks[1]),
                (7, blocks[2]),
                (40, 1),    # DIMSCALE
                (41, attrib["arrow size"]),    # DIMASZ (arrow size) 
                (42, 200),    # DIMEXO (Extension line offset)
                (43, 0),    # DIMDLI #DIMENSION LINE INCREMENT
                (44, 15),    # DIMEXE EXTENSION LINE EXTENSION
                (45, 0),    # DIMRND (ROUNDING VALUE FOR DIMENSION DISTANCES
                (46, 0),    # DIMDLE
                (47, 0),    # DIMTP PLUS TOLERANCE
                (48, 0),    # DIMTM MINUS TOLERANCE
                (140, attrib["text height"]),   # DIMTXT
                (141, 0),   # DIMCEN SIZE OF CENTER MARK / LINES
                (142, 0),   # DIMTSZ DIMENSIONING TICK SIZE
                (143, 23.4),# DIMALTF ALTERNATE UNIT SCALE FACTOR
                (144, 1),   # DIMLFAC LINEAR MEASUREMENTS SCALE FACTIR 
                (145, 0),   # DIMTVP TEXT VERTICAL POSITION
                (146, 1),   # DIMTFAC DIMENSION TOLERANCE DISPLAY SCALE FACTOR
                (147, attrib["text offset"]),   # DIMGAP DIMENSION LINE GAP 
                (71, 0),    # DIMTOL DIMENSION TOLERANCE GENERATED IF NONZERO
                (72, 0),    # DIMLIM DIMENSION LIMITS GENERATED IF NONZERO
                (73, 0),    # DIMTIH TEXT INSIDE HORIZONTAL IF NONZERO
                (74, 0),    # DIMTOH TEXT OUTSIDE HORIZONTAL IF NONZERO
                (75, 1),    # DIMSE1 FIRST EXTENSION LINE SUPPRESSED IF NONZERO 
                (76, 1),    # DIMSE2
                (77, 1),    # DIMTAD TEXT ABOVE DIMENSION LINE IF NONZERO
                (78, 8),    # DIMZIN CONTROL SUPPRESSION OF ZEROS FOR TOLERANCE VALUES
                (170, 0),   # DIMALT ALTERNATE UNIT DIMENSION PERFORMED IF NONZERO
                (171, 2),   # DIMALTD ALTERNATE UNIT DECIMAL PLACE
                (172, 0),   # DIMTOFL IF TEXT IS OUTSIDE EXTENSIONS, FORCE LINE EXTENSUIONS BETWEEN EXTENSIONS IF NONZERO
                (173, 1),   # DIMSAH USE SEPARATE ARROW BLOCKS IF NONZERO
                (174, 1),   # DIMTIX FORCE TEXT INSIDE EXTENSIONS IF NONZERO
                (175, 0),   # DIMSOXD SUPPRESS OUTSIUDE EXTENSIONS DIMENSION LINES IF NONZERO
                (176, attrib["dim color"]), # DIMCLRD DIMENSION LINE COLOR
                (177, attrib["dim ext color"]), # DIMCLRE DIMENSION EXTENSION LINE COLOR 
                (178, attrib["dim text color"]), # DIMCLRT DIMENSION TEXT COLOR
                (280, 0)    # HORIZONTAL POSITION
                ] 
        self.list_code = filter_list(list)

class TableBlockRecord:
    
    def __init__(self, block_name ):
        self.handle = handle_counter.get_handle()
        self.begin = [(0, "BLOCK_RECORD")]
        list = [ (2, block_name),    # Name of the block representing dimstyle blocks
                 (5, self.handle) ]  # Handle of the block records
        self.list_code = filter_list(list)
    
class Entities:
    
    def __init__(self, entities=[], handle=None, subclass_marker=None):
        self.begin = [(2,"ENTITIES")]
        self.list_code = ""
        
        for each_entity in entities:
            self.list_code += list_scan(each_entity.list_common_code+each_entity.list_code)

    def write(self):
        return section(list_scan(self.begin)+self.list_code)
    
class Entity:
    
    def __init__(self, entity_type, layer, linetype_name=None, color=None):
        self.handle = handle_counter.get_handle()
        list = [(0,  entity_type), 
                (5,  self.handle),
                (8,  layer),                
                (6,  linetype_name),        # If it is None, the default will be "BYLAYER"
                (62, color)]                # If it is None, the default will be "BYLAYER"
        self.list_common_code = filter_list(list)

class Insert(Entity):
    def __init__(self, block_name, layer, p1, scale = (None,None), rotation_angle=None):
        Entity.__init__(self, "INSERT", layer)
        list = [(2,  block_name),
                          (10, p1[0]),
                          (20, p1[1]),
                          (30, 0),
                          (41, scale[0]),
                          (42, scale[1])]
        if scale !=(None,None):
            list.append((43, 1.0))
        list += [(50, rotation_angle)]
        self.list_code = filter_list(list)
    
class Line(Entity):
    def __init__(self, p1, p2,  layer, linetype_name=None,thickness=None, scale_coeff = 1.0, p=(0,0), handle=None, color = None):        
        Entity.__init__(self, "LINE", layer, linetype_name, color = color)
        list = [ (39, thickness),         # Thickness
                 (10, p1[0]*scale_coeff+p[0]),             # X start point
                 (20, p1[1]*scale_coeff+p[1]),             # Y start point
                 (30, 0),                 # Z start point  
                 (11, p2[0]*scale_coeff+p[0]),             # X end point
                 (21, p2[1]*scale_coeff+p[1]),             # Y end point
                 (31, 0) ]                # Z end point
        self.list_code = filter_list(list)
        
class Dimension(Entity):
    def __init__(self, block, p1, p2, p3,p4, layer, measure, style, block_list, dim_type = 0, scale_coeff = 1.0, angle = 0, p = (0,0)):
        Entity.__init__(self, "DIMENSION", layer)
        list = [ (2, block),
                 (10, p1[0]*scale_coeff+p[0]),             # X start point
                 (20, p1[1]*scale_coeff+p[1]),             # Y start point
                 (30, 0),                 # Z start point  
                 (11, p2[0]*scale_coeff+p[0]),             # X end point
                 (21, p2[1]*scale_coeff+p[1]),             # Y end point
                 (31, 0),
                 (70, dim_type),
                 (13, p3[0]*scale_coeff+p[0]),             # X end point
                 (23, p3[1]*scale_coeff+p[1]),             # Y end point
                 (33, 0),
                 (14, p4[0]*scale_coeff+p[0]),             # X end point
                 (24, p4[1]*scale_coeff+p[1]),             # Y end point
                 (34, 0),
                 #|(50, angle),

#                 (1001,"ACAD"),
#                 (1000, "DSTYLE"),
#                 (1002, "{"),
#                 (1070, 7),
#                 (1000, block_list[2]),
#                 (1070, 5),
#                 (1000, " "),
#                 (1070, 6),
#                 (1000, block_list[1]),
#                 (1002, "}")
                 
                 ]
        self.list_code = filter_list(list)
        
        def write(self):
            return list_scan(self.list_common_code+self.list_code)
        
class Circle(Entity):
    def __init__(self, p1, radius, layer, scale_coeff = 1.0,thickness=None, surface= False, color = None):
        if not surface:
            Entity.__init__(self, "CIRCLE", layer, color= color)
            list = [(39, thickness), 
                  (10,  p1[0]),
                  (20,  p1[1]),
                  (30,  0),
                  (40,  radius * scale_coeff),
                  (100, "AcDbCircle")]
            
        else:
            Entity.__init__(self, "POLYLINE", layer)
            cerchio = Polyline([( p1[0] - radius * scale_coeff / 2.0, p1[1]), ( p1[0] + radius * scale_coeff / 2.0, p1[1]) ], layer="SD-Testi", flag="Closed", start_width=radius * scale_coeff, end_width = radius * scale_coeff)
            list = cerchio.list_code
            self.common_code = filter_list(cerchio.list_common_code)  
        self.list_code = filter_list(list)    
        
class Text(Entity):
    def __init__(self, text_height, string, p1, p2=(0,0), layer=None, text_style_name=None, 
                   thickness=None, text_rotation=None, rel_x_scale_factor=None, oblique_angle=None,
                  text_generation_flag=None, horiz_just=None, vert_just=None, color = None):
                 
        Entity.__init__(self, "TEXT", layer, color = color)
        string = str(string)
        map_horiz = {"Left":0,
                     "Center":1,
                     "Right":2,
                     "Aligned":3,
                     "Middle":4}
        
        map_vert = {"Baseline":0,
                    "Bottom":1,
                    "Middle":2,
                    "Top":3}
        
        list = [  (39, thickness),
                  (10, p1[0]),
                  (20, p1[1]),
                  (30, 0),
                  (11, p2[0]),
                  (21, p2[1])]
        
        if p2 != (None, None):
            list.append((31, 0))
            
        list += [ (40, text_height),
                  (1,  string),
                  (50, text_rotation),
                  (41, rel_x_scale_factor),
                  (51, oblique_angle),
                  (7,  text_style_name),
                  (71, text_generation_flag)]
        
        if horiz_just is not None:
            list.append((72, map_horiz[horiz_just]))
        if vert_just is not None:
            list.append((73, map_vert[vert_just]))
        
        self.list_code = filter_list(list)
        
    def write(self):
        return list_scan(self.list_common_code+self.list_code)

class Vertex(Entity):
    def __init__(self, p1, layer, scale = 1.0, p=(0,0),bulge=None):
        Entity.__init__(self, "VERTEX", layer)
        list_code  =  [(10,  p1[0]*scale+p[0]),
                       (20,  p1[1]*scale+p[1]),
                       (30,  0),
                       (42, bulge)]
        self.list_code = filter_list(list_code)
    
class Polyline(Entity):
    def __init__(self,  vertex_list, layer,  scale_coeff = 1.0, thickness=0, flag="Default", start_width=None, end_width=None,p = (0,0), color = None):
        Entity.__init__(self, "POLYLINE", layer, color = color)
        map_flag = {"Default":"0",
                    "Closed":"1",
                    "Curve-fit":"10",
                    "Spline-fit":"100",
                    "3D":"1000",
                    "3D mesh":"10000",
                    "Mesh closed N dir":"100000",
                    "Polyface":"1000000",
                    "Linepattern":"10000000"}
        
        val_flag = map_flag[flag]
        
        list_code  =  [(10,  0),
                       (20,  0),
                       (30,  0),
                       (40, start_width),
                       (41, end_width),
                       (39,  thickness),
                       (70,  val_flag),
                       (66, 1),
                       (100, "AcDb2dPolyline")]

        for each_vertex in vertex_list:
            
            
            if flag=="Closed":
                vertex = Vertex((each_vertex[0], each_vertex[1]), layer, scale_coeff,p, bulge=1)
            else:
                vertex = Vertex((each_vertex[0], each_vertex[1]), layer, scale_coeff, p )
                
            list_code += vertex.list_common_code+vertex.list_code
        list_code += [(0, "SEQEND"),(8,layer)]
        self.list_code = filter_list(list_code)
        
    def write(self):
        list_scan(self.list_common_code+self.list_code)
 
class HandleCounter:
    def __init__(self):
        self.counter = 0
    def get_handle(self):
        self.counter += 1
        return str(hex(self.counter))[2:]

def rotation(seq_vertexes, angle, p, scale_coeff = 1.0):
    vertexes = []
    angle = angle * pi / 180.0
    
    for x,y in seq_vertexes:
        vertexes.append((p[0] + (x * cos(angle) - y * sin(angle)) * scale_coeff, p[1] + (x * sin(angle) + y * cos(angle)) * scale_coeff))
    return vertexes

def scale(seq_vertexes, factor, p = (0,0)):
    vertexes = []
    
    for (x, y) in seq_vertexes:
        vertexes.append((p[0]+factor*x, p[1]+factor*y ))
    return vertexes
    
def translation(seq_vertexes,  p):
    vertexes = []
    
    for x, y in seq_vertexes:
        vertexes.append((p[0]+x, p[1]+y))

    return vertexes

def seq_polylines(seq_vertices, p1, layer, scale_coeff=1.0, thickness=0, flag="Default", start_width=None, end_width=None, p2=(0,0), color=None):
    polylines = []

    for vertexes in seq_vertexes:
        polylines.append( Polyline( vertexes, layer, scale_coeff, thickness, flag, start_width, end_width, p1), color )
    
    return polylines
    
def seq_lines(vertexes, layer, scale_coeff=1.0, color=None, p=(0,0)):
    lines = []
    i = 0
    
    for each_vertex in vertexes:
        
        if i % 2 == 1:
            v1 = ( each_vertex[0] + p[0], each_vertex[1] + p[1] )
            v2 = ( prec_vertex[0] + p[0], prec_vertex[1] + p[1] )
            lines.append( Line( v1, v2, layer, scale_coeff = scale_coeff, color = color ) )
        i += 1
        prec_vertex = each_vertex

    return lines

def list_scan(list):
    string = ""
    
    for each_elem in list:
        string+=str(each_elem[0])+"\n"+str(each_elem[1])+"\n"
    return string

def section(section):
        """ It inserts wrapping lines of every kind of sections """
        begin = "0\nSECTION\n"
        end = "0\nENDSEC\n"
        return begin+section+end

def filter_list(list):
    list_filtered = []
    
    for each_tuple in list:
        
        if each_tuple[1] is not None:
            list_filtered.append(each_tuple)
            
    return list_filtered

#def display(elemento, x=0, y=0, assoluto=False):
#    """ Disegna l'elemento senza modificare la matrice di trasformazione corrente, traslandolo su un piano 2D"""
#    #glTranslatef(elemento.x_elem, elemento.y_elem, 0)
#    
#    elemento.display((x, y))
#    return elemento.entities
    
def display_stile(stile, layer, (x,y), scala = 1.0, scale_coeff = 1.0, color = 1, angolo = 0, posizione = None):
    unita = 0.5 * scala

    if stile == "Quadrato":
        p1, p2, p3, p4 = rotation( [(-unita, -unita), (unita, -unita), (unita, unita), (-unita, unita)], angolo, (x,y), color = color)
        style=Polyline([p1, p2, p3, p4], layer, flag="Closed", color = color)
        
    elif stile=="Cerchio":
        style = Circle((x,y), unita, layer, surface=True, scale_coeff = scale_coeff)
        
    elif stile=="Segmento":
        
        if posizione == "Primo":
            p1, p2 = rotation( [(0, 0), (+unita, 0)], angolo, (x,y))
            
        elif posizione == "Ultimo":
            p1, p2 = rotation( [(0, 0), (-unita, 0)], angolo, (x,y))
            
        else:
            p1, p2 = rotation( [(-unita, 0), (+unita, 0)], angolo, (x,y))
        style = Line( p1, p2, layer, color = color)
        
    elif stile=="Segmento obliquo (\)":
         p1, p2 = rotation( [(unita,-unita), (-unita, +unita)], angolo, (x,y))
         style=Line( p1, p2, layer, color = color)
         
    elif stile=="Segmento obliquo (/)":
         p1, p2 = rotation( [(unita, unita), (-unita, -unita)], angolo, (x,y))
         style=Line(p1, p2, layer, color = color)
    else:
        style = None
        
    return style 

handle_counter = HandleCounter()
