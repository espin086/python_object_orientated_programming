#!/usr/bin/env python
# coding: utf-8

# # Notebook 

# In[2]:


#store the next available id for all new notes
import datetime
last_id = 0


# ## Note Class

# In[4]:


class Note:
    '''Represents a note in a notebook. Match against a string of searches
    and store tags for each note'''
    
    def __init__(self, memo, tags=''):
        '''iniitialize a note with memo and optional space-separated tags. 
        Automatically set the note's creation date and unique id.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
        
    def match(self, filter):
        '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise
        
        Search is case sensitive and matches both text and tags.
        '''
        return filter in self.memo or filter in self.tags
        


# ## Notebook Class

# In[9]:


class Notebook:
    '''Represents a collection of notes that can be tagged, modified, and searched'''
    
    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []
        
    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo, tags))
        
    def _find_note(self, note_id):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if note.id == note_id:
                return note
        return None
        
    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and change its memo to the given value'''
        self._find_note(note_id).memo = memo
        
                
    def modify_tags(self, note_id, tags):
        '''find the note with the given id and change its tags to the given value'''
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break
                
    def search(self, filter):
        '''Find all notes that match the given filter string.'''
        return [note for note in self.notes if note.match(filter)]
          


# ### Convert to Python Executable

# In[13]:


#!ipython nbconvert --to=python notebook.ipynb


# In[ ]:




